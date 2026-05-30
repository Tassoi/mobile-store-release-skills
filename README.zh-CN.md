# Mobile Store Release Skills

[![Validate skills](../../actions/workflows/validate.yml/badge.svg)](../../actions/workflows/validate.yml)

一组可复用的 Codex skills，用于准备和检查移动应用在 Apple App Store 与 Google Play 的发布流程。

这些 skills 不绑定具体项目。它们会先读取当前仓库的发布工具和配置，例如 fastlane、Flutter、React Native、native iOS、native Android，再根据仓库事实生成发布前检查清单和风险提示。

## 快速开始

```sh
git clone https://github.com/Tassoi/mobile-store-release-skills.git
cd mobile-store-release-skills
python3 scripts/validate_skills.py
```

安装 skills：

```sh
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS_DIR"
cp -R skills/app-store-release "$CODEX_SKILLS_DIR/"
cp -R skills/google-play-release "$CODEX_SKILLS_DIR/"
cp -R skills/mobile-release-coordinator "$CODEX_SKILLS_DIR/"
```

然后进入你的移动应用仓库，向 Codex 发起请求：

```text
Use $mobile-release-coordinator to check whether this app is ready for store release.
```

## Skills

- `app-store-release`：App Store Connect、TestFlight、iOS 签名、metadata、隐私、审核准备。
- `google-play-release`：Google Play Console、Android App Bundle、签名、测试轨道、Data safety、发布准备。
- `mobile-release-coordinator`：跨平台发布入口，先判断平台与发布工具，再分发到对应 skill。

## 仓库结构

```text
skills/        可安装的 Codex skills。
examples/      匿名化示例，可参考结构，但需要替换占位值。
fixtures/      匿名化验证夹具，故意包含发布风险，不要复制到真实 App。
tests/golden/  每个 release-risk fixture 的最低期望发现项。
scripts/       仓库校验脚本。
.github/       CI、issue templates、PR template。
```

## 支持矩阵

| 范围 | 状态 | 说明 |
| --- | --- | --- |
| Flutter + iOS fastlane | Supported | 识别 TestFlight/App Store lane、metadata、截图、提交审核、自动发布风险。 |
| Flutter + Android Gradle | Supported | 检查版本、release signing、AAB、权限、cleartext traffic、Play 发布准备。 |
| Flutter without fastlane | Supported | 不编造上传自动化，提示手动 Store Console 或 CI 路径。 |
| Generic iOS fastlane | Supported | 先读取真实 lane 和参数，再建议命令。 |
| Generic Android fastlane | Supported | 读取真实 track、rollout、metadata 和 service account 假设。 |
| Native iOS | Partial | 支持通用 App Store / Xcode 检查，已有 fixture 覆盖。 |
| Native Android | Partial | 支持通用 Gradle / Play 检查，已有 fixture 覆盖。 |
| React Native | Planned | 需要匿名化 fixture 和 references。 |
| Expo/EAS | Planned | 需要 EAS 专用 references 和 fixtures。 |

## 安全模型

- 先检查仓库事实，再给建议；不编造 fastlane lane、Gradle task 或 Store Console 状态。
- 除非用户明确要求执行，否则不运行生产发布命令。
- 提交审核、自动发布、production rollout、签名变更都视为高风险操作。
- 涉及时效性平台政策时，必须根据各平台 `references/official-sources.md` 和官方链接核对。
- 不提交真实凭据、私有 bundle id / package name、webhook、Store Console 截图或组织内部发布数据。

## Fixtures 与 Golden Expectations

`fixtures/` 是用于验证的匿名化项目切片。它们故意包含发布风险，帮助 CI 防止 skill 回归。不要把 fixtures 复制到真实 App。

当前 fixtures：

- `flutter-release-risk`：Flutter + iOS fastlane + Android Gradle 发布风险。
- `native-ios-release-risk`：native iOS、privacy manifest、entitlements、审核敏感权限。
- `native-android-release-risk`：native Android Gradle、release signing、权限、cleartext traffic。

`tests/golden/` 记录每个 fixture 至少应该被识别出的发现项。它们不是自动生成结果，而是用来固定 skill 行为期望。

## 校验

```sh
python3 scripts/validate_skills.py
```

validator 会检查：

- skill frontmatter 与 UI metadata
- reference 链接和 orphan reference
- fixtures 与 golden expectations
- README 支持矩阵
- GitHub governance 文件
- 常见凭据或私有标识泄漏

## 贡献

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [SECURITY.md](SECURITY.md)。

如果修改 Apple 或 Google Play 政策相关内容，请在 PR 中链接官方来源。不要提交真实密钥、真实 App 标识、service account JSON、keystore、webhook 或 Store Console 截图。

## 变更记录

见 [CHANGELOG.md](CHANGELOG.md)。
