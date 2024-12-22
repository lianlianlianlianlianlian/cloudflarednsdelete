#!/bin/bash
# 配置部分：请替换成你的 Cloudflare API Token 和 Zone ID
API_TOKEN="your_cloudflare_api_token"
ZONE_ID="your_cloudflare_zone_id"
DOMAIN="yourdomain.com" # 要删除 DNS 记录的域名

# 获取所有 DNS 记录的列表
echo "获取 Cloudflare 中域名 $DOMAIN 的所有 DNS 记录..."
RECORDS=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?name=$DOMAIN" \
-H "Authorization: Bearer $API_TOKEN" \
-H "Content-Type: application/json")

# 检查请求是否成功
STATUS_CODE=$(echo $RECORDS | jq -r '.success')
if [[ "$STATUS_CODE" == "false" ]]; then
  ERROR_MESSAGE=$(echo $RECORDS | jq -r '.errors[].message')
  echo "请求失败: $ERROR_MESSAGE"
  exit 1
fi

# 获取 DNS 记录 ID 列表
RECORD_IDS=$(echo $RECORDS | jq -r '.result[].id')

# 如果没有找到 DNS 记录
if [ -z "$RECORD_IDS" ]; then
  echo "没有找到任何 DNS 记录。"
  exit 0 # 这里改为0，表示没有记录可删，不是错误
fi

# 循环删除每个 DNS 记录
echo "开始删除 DNS 记录..."
for RECORD_ID in $RECORD_IDS; do
  echo "正在删除 DNS 记录 ID: $RECORD_ID ..."
  DELETE_RESPONSE=$(curl -s -X DELETE "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records/$RECORD_ID" \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json")
  # 检查删除是否成功
  if echo $DELETE_RESPONSE | jq -e '.success' > /dev/null 2>&1; then
    echo "删除成功: DNS 记录 ID $RECORD_ID"
  else
    echo "删除失败: DNS 记录 ID $RECORD_ID -  $(echo $DELETE_RESPONSE | jq -r '.errors[].message')"
  fi
done
echo "所有 DNS 记录已删除。"