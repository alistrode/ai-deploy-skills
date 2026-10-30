#!/usr/bin/env python3
"""Minimal, opt-in text inference probe. Never accepts keys in argv."""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    parser = argparse.ArgumentParser(description="先输出无凭据计划；--execute 才真正调用文本模型")
    parser.add_argument("--protocol", required=True, choices=["openai-chat", "openai-responses", "anthropic-messages"])
    parser.add_argument("--url", required=True, help="从当前官方文档获取完整端点，不是仅 base URL")
    parser.add_argument("--model", required=True)
    parser.add_argument("--key-env", required=True, help="包含密钥的环境变量名，不是密钥本身")
    parser.add_argument("--anthropic-version", help="Messages 协议必须从当前文档确定版本头")
    parser.add_argument("--limit-field", choices=["max_tokens", "max_completion_tokens", "max_output_tokens"], help="仅在该模型官方文档支持时指定")
    parser.add_argument("--limit", type=int, default=128)
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    url = urllib.parse.urlsplit(args.url)
    if url.username or url.password or url.query or url.fragment or not url.hostname:
        parser.error("端点不得包含用户信息、查询密钥或 fragment")
    if url.scheme != "https" and not (url.scheme == "http" and url.hostname in ("localhost", "127.0.0.1", "::1")):
        parser.error("远端端点必须使用 HTTPS；本地推理仅允许 loopback HTTP")
    if not 1 <= args.limit <= 4096:
        parser.error("探测输出限制必须在 1..4096")
    if args.protocol == "anthropic-messages" and not args.anthropic_version:
        parser.error("Messages 协议需要 --anthropic-version，值从官方文档获取")
    prompt = "Reply only with READY."
    body = {"model": args.model}
    if args.protocol == "openai-responses":
        body["input"] = prompt
    else:
        body["messages"] = [{"role": "user", "content": prompt}]
    if args.protocol == "anthropic-messages":
        body["max_tokens"] = args.limit
    elif args.limit_field:
        body[args.limit_field] = args.limit
    if not args.execute:
        print(json.dumps({"executed": False, "method": "POST", "url": args.url, "protocol": args.protocol, "body": body, "credential_source": "environment variable name supplied; value not read", "note": "先核对官方端点、模型、计费与授权。--execute 才读取密钥并发送一次请求。"}, ensure_ascii=False, indent=2))
        return
    key = os.environ.get(args.key_env)
    if not key:
        print(json.dumps({"status": "blocked-auth", "message": "指定环境变量未提供凭据；未发送请求。"}, ensure_ascii=False))
        sys.exit(2)
    headers = {"Content-Type": "application/json"}
    if args.protocol == "anthropic-messages":
        headers.update({"x-api-key": key, "anthropic-version": args.anthropic_version})
    else:
        headers["Authorization"] = "Bearer " + key
    req = urllib.request.Request(args.url, data=json.dumps(body).encode(), headers=headers, method="POST")
    try:
        with urllib.request.build_opener(NoRedirect()).open(req, timeout=60) as response:
            raw = response.read(2 * 1024 * 1024 + 1)
            if len(raw) > 2 * 1024 * 1024:
                raise ValueError("response too large")
            result = json.loads(raw)
        if args.protocol == "openai-chat":
            content = result.get("choices", [{}])[0].get("message", {}).get("content")
        elif args.protocol == "anthropic-messages":
            content = "".join(x.get("text", "") for x in result.get("content", []) if x.get("type") == "text")
        else:
            content = "".join(c.get("text", "") for item in result.get("output", []) for c in item.get("content", []) if c.get("type") == "output_text")
        if not isinstance(content, str) or not content.strip():
            print(json.dumps({"status": "failed", "message": "有响应但未提取到有效文本；按官方协议检查原任务，不宣称可用。"}, ensure_ascii=False))
            sys.exit(3)
        print(json.dumps({"status": "ready", "model": args.model, "response_model": result.get("model"), "output_excerpt": content.replace(key, "[REDACTED]")[:400], "scope": "one_text_inference_only"}, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as error:
        # Do not dump response bodies or headers: some gateways reflect credentials.
        print(json.dumps({"status": "failed", "http_status": error.code, "message": "按文档检查权限、模型、额度与端点；未自动重试或切换收费渠道。"}, ensure_ascii=False))
        sys.exit(4)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, KeyError, IndexError, TypeError):
        print(json.dumps({"status": "failed", "message": "网络或协议异常；未输出私密请求或异常内容。先查询原操作状态。"}, ensure_ascii=False))
        sys.exit(5)


if __name__ == "__main__":
    main()
