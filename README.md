# Cloudflare DNS 记录删除脚本

一个用于批量删除 Cloudflare 特定域名下所有 DNS 记录的 Bash 脚本。本脚本通过 Cloudflare API 操作，需提供 API Token 和 Zone ID 进行身份验证。

## 功能特性

- 自动获取并删除指定域名下的所有 DNS 记录。
- 提供详细的操作日志，方便查看。
- 具备完善的错误处理机制，输出清晰的错误信息。
- 配置简单，易于使用。

---

## 先决条件

1. **Cloudflare API Token**  
   请生成一个具有以下权限的 API Token：
   - `Zone:Read`：获取 DNS 记录。
   - `Zone:Edit`：删除 DNS 记录。

   [Cloudflare API Token 生成指南](https://developers.cloudflare.com/api/tokens/create/)

2. **Zone ID**  
   你可以在 Cloudflare 仪表盘中找到 Zone ID，路径为 **Overview** 标签页。

3. **依赖工具**  
   本脚本需要以下工具：
   - `curl`
   - `jq`（JSON 解析工具）

---

## 安装

1. 克隆本仓库：
   ```bash
   git clone https://github.com/lianlianlianlianlianlian/cloudflarednsdelete.git
   cd cloudflarednsdelete
   ```

2. 赋予脚本可执行权限：
   ```bash
   chmod +x delete.sh
   ```

---

## 配置

编辑脚本，设置你的 API Token、Zone ID 和域名信息。将以下占位符替换为你的实际值：

```bash
API_TOKEN="your_cloudflare_api_token"
ZONE_ID="your_cloudflare_zone_id"
DOMAIN="yourdomain.com" # 要删除 DNS 记录的域名
```

---

## 使用方法

运行以下命令执行脚本：

```bash
./delete.sh
```

### 脚本流程：
1. 获取指定域名下的所有 DNS 记录。
2. 遍历记录并逐一删除。
3. 输出每次操作的日志。

---

## 输出示例

### 成功：
```bash
获取 Cloudflare 中域名 example.com 的所有 DNS 记录...
开始删除 DNS 记录...
正在删除 DNS 记录 ID: abc123...
删除成功: DNS 记录 ID abc123
所有 DNS 记录已删除。
```

### 失败：
```bash
获取 Cloudflare 中域名 example.com 的所有 DNS 记录...
请求失败: Invalid access token
```

---

## 错误处理

本脚本处理以下常见场景：
- 未找到 DNS 记录。
- 提供的 API Token 或 Zone ID 无效。
- API 请求失败。

每种错误都会输出详细信息，帮助你快速排查问题。

---

## 贡献

欢迎提交 Issue 或 Pull Request 来改进本脚本或添加新功能。你也可以 Fork 此仓库进行修改。

---

## 许可证

本项目基于 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

