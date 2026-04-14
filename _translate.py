#!/usr/bin/env python3
"""Translate step files and issue files for integrate-mcp-with-copilot."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

files = {}

# Step 1
files[".github/steps/1-step.md"] = r"""## Step 1: MCP 소개 및 환경 설정

<img width="150" align="right" alt="copilot logo" src="https://github.com/user-attachments/assets/4d22496d-850b-4785-aafe-11cba03cd5f2" />

[GitHub Copilot 시작하기](https://github.com/skills-kr/getting-started-with-github-copilot) 실습에서 학생들이 이벤트에 등록할 수 있는 Mergington 고등학교의 과외 활동 웹사이트를 소개받았습니다.

그런데 이제 문제가 생겼습니다... 하지만 좋은 문제입니다! 더 많은 선생님들이 이 사이트를 사용하고 싶어합니다! 🎉

동료 선생님들은 아이디어가 넘치지만 모든 요청을 처리하기가 벅찹니다! 😮 이 문제를 해결하기 위해, Model Context Protocol (MCP)을 활성화하여 GitHub Copilot을 업그레이드해 봅시다. 구체적으로, GitHub MCP 서버를 추가하여 이슈 관리와 웹사이트 업그레이드를 결합한 워크플로우를 만들겠습니다. 🧑‍🚀

시작해 봅시다!

### 📖 이론: Model Context Protocol (MCP)이란?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)은 흔히 "AI를 위한 USB-C"라고 불립니다 - GitHub Copilot(및 기타 AI 도구)이 다른 서비스와 원활하게 상호작용할 수 있게 하는 범용 커넥터입니다.

본질적으로, 서비스의 기능과 요구 사항을 설명하는 방법으로, AI 도구가 어떤 메서드를 사용할지 쉽게 결정하고 매개변수를 정확하게 제공할 수 있습니다. MCP 서버가 그 인터페이스를 제공합니다.

```mermaid
graph LR
    A[개발자] -->|사용| B[GitHub Copilot]
    B -->|통합 API| MCP[Model Context Protocol]

    MCP <-->|고유 API| C[(GitHub)]
    MCP <-->|고유 API| D[(Slack)]
    MCP <-->|고유 API| E[(Figma)]

    style B fill:#4CAF50,stroke:#333,stroke-width:2px

    subgraph "컨텍스트 전환 줄이고, 코딩에 집중"
        B
        MCP
        C
        D
        E

    end
```

### :keyboard: 활동: 개발 환경 알아보기

MCP에 들어가기 전에, 개발 환경을 시작하고 과외 활동 애플리케이션을 다시 살펴봅시다.

1. 아래 버튼을 우클릭하여 새 탭에서 **Create Codespace** 페이지를 엽니다. 기본 구성을 사용하세요.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)

1. **Copilot Chat** 및 **Python** 확장이 설치되고 활성화되어 있는지 확인합니다.

   <img width="300" alt="copilot extension for VS Code" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />

1. 수정 전에 애플리케이션이 실행되는지 확인합니다. 왼쪽 사이드바에서 **Run and Debug** 탭을 선택한 후 **Start Debugging** 아이콘을 누릅니다.

   <details>
   <summary>📸 스크린샷 보기</summary><br/>

   <img width="300" alt="run and debug" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />

   </details>

   <details>
   <summary>🤷 문제가 있나요?</summary><br/>

   **Run and Debug** 영역이 비어있다면, VS Code를 다시 로드해 보세요: 명령 팔레트(`Ctrl`+`Shift`+`P`)를 열고 `Developer: Reload Window`를 검색합니다.

   <img width="300" alt="empty run and debug panel" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>

1. **Ports** 탭에서 웹페이지 주소를 찾아 열고, 실행 중인지 확인합니다.

   <details>
   <summary>📸 스크린샷 보기</summary><br/>

   <img width="350" alt="ports tab" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   ![Screenshot of Mergington High School WebApp](https://github.com/user-attachments/assets/5cb88d53-d948-457e-9f4b-403d697fa93a)

   </details>

### :keyboard: 활동: GitHub MCP 서버 추가하기

1. Codespace 안에서 **Copilot Chat** 패널을 열고 **Agent** 모드가 선택되어 있는지 확인합니다.

   <img width="200" alt="image" src="https://github.com/user-attachments/assets/201e08ab-14a0-48bf-824e-ba4f8f43f8ab" />

   <details>
   <summary>에이전트 모드가 없나요?</summary><br/>

   - VS Code가 최소 `v1.99.0`인지 확인합니다.
   - Copilot 확장이 최소 `v1.296.0`인지 확인합니다.
   - [사용자 또는 워크스페이스 설정](https://code.visualstudio.com/docs/configure/settings#_workspace-settings)에서 에이전트 모드가 활성화되어 있는지 확인합니다.

      <img width="300" alt="image" src="https://github.com/user-attachments/assets/407a79dd-707e-471b-b56b-1938aece4ad8" />

   </details>

1. Codespace 안에서 `.vscode` 폴더로 이동하여 `mcp.json`이라는 새 파일을 만듭니다. 다음 내용을 붙여넣으세요:

   📄 **.vscode/mcp.json**

   ```json
   {
     "servers": {
       "github": {
         "type": "http",
         "url": "https://api.githubcopilot.com/mcp/"
       }
     }
   }
   ```

1. `.vscode/mcp.json` 파일에서 **Start** 버튼을 클릭하고 GitHub로 인증하라는 프롬프트를 수락합니다. 이것으로 GitHub Copilot에 MCP 서버의 기능을 알려줬습니다.

   <img width="350" alt="mcp.json file showing start button" src="https://github.com/user-attachments/assets/15a3d885-1c13-40b4-8d59-87b478ddd8a0" />

   <img width="350" alt="allow authentication prompt" src="https://github.com/user-attachments/assets/f5ec128d-9924-454b-8ab4-3f43ebc83cfc" /><br/>

   <img width="350" alt="mcp.json file showing running server" src="https://github.com/user-attachments/assets/c413c52d-94dc-429f-91e0-3486141908b9" />

1. Copilot 사이드 패널에서 **🛠️ 아이콘**을 클릭하여 추가 기능을 확인합니다.

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/b1be8b80-c69c-4da5-9aea-4bbaa1c6de10" />

   <img width="350" alt="image" src="https://github.com/user-attachments/assets/99178d1b-adbe-4cf4-ab9c-3a4d29918a13" />

1. `.vscode/mcp.json` 파일을 `main` 브랜치에 **커밋**하고 **푸시**합니다.

   > 🪧 **참고:** `main`에 직접 푸시하는 것은 권장되지 않습니다. 이 실습을 단순화하기 위한 것입니다.

1. MCP 서버 구성이 GitHub에 푸시되었으므로 Mona가 이미 작업을 확인하고 있을 것입니다. 잠시 기다리며 댓글을 확인하세요. 진행 상황과 다음 레슨이 표시됩니다.

> [!NOTE]
> 다음 단계에서는 GitHub 이슈를 생성합니다. 알림 이메일을 피하려면 저장소의 Watch를 해제할 수 있습니다.

<details>
<summary>문제가 있나요?</summary><br/>

다음을 확인하세요:

- `.vscode/mcp.json` 파일이 제공된 예시와 유사한지 확인합니다.
- 변경사항을 `main` 브랜치에 푸시했는지 확인합니다.

</details>
"""

# Step 2
files[".github/steps/2-step.md"] = r"""## Step 2: 에이전트 모드와 GitHub용 MCP 서버

잘 하셨습니다! 방금 첫 번째 MCP 서버를 GitHub Copilot에 연결했습니다! 🎉

🚨 선생님들이 버그와 기능 요청으로 저장소에 새 이슈를 열었습니다! [확인해 보세요](https://github.com/{{full_repo_name}}/issues) - 좋은 아이디어가 너무 많습니다!

이슈들을 살펴보고 다른 업그레이드도 조사를 시작해야 할 것 같습니다. 다행히도 GitHub용 MCP 서버가 있으니, 이슈를 분류하고 앞서나가기 위한 조사도 꽤 빠르게 할 수 있습니다! 🕵️

### 📖 이론: 에이전트 모드에서 MCP 도구 호출이 작동하는 방식

이제 GitHub MCP가 연결되었으니, **에이전트 모드**가 실제로 이런 외부 도구를 어떻게 사용하는지 살펴봅시다.

프롬프트를 보낼 때마다 Copilot은 사용 가능한 도구의 카탈로그(목록 + 스키마)도 함께 포함합니다. 그러면 Copilot이 계획하고 결정합니다:

- 이 요청에 도구가 필요한가?
- 어떤 도구가 의도에 가장 잘 맞는가?
- 각 도구의 입력 스키마에 따라 어떤 인수를 전달해야 하는가?

그런 다음 Copilot이 선택한 도구를 호출하고 결과를 LLM에 스트리밍합니다.

![Flowchart diagram illustrating how a user interacts with Copilot Agent Mode](https://github.blog/wp-content/uploads/2025/05/how-it-works.png)

> [!TIP]
> 프롬프트에 `#<tool_name>`을 포함하여 Copilot이 특정 도구를 호출하도록 명시적으로 유도할 수도 있습니다 (예: `#create_pull_request`, `#codebase`).

여기서 Copilot은 GitHub 인식 도구 세트를 사용하여 레포의 코드를 읽거나 편집하는 것 이상의 작업을 수행할 수 있습니다. 다음과 같은 요청이 가능합니다:

- 영감을 얻기 위해 유사한 공개 프로젝트를 발견합니다.
- 설명, 댓글, 좋아요를 고려하여 이슈를 검색합니다.
- 마음에 드는 새 아이디어를 즉시 이슈로 만들어 놓치지 않도록 합니다.
- 이슈를 가져오고, 브랜치에서 변경하고, 풀 리퀘스트를 시작합니다.

멋지지 않나요?! 이제 실행해 봅시다! 👩‍🚀

### :keyboard: 활동: 빠르게 아이디어 찾기 및 저장하기

GitHub MCP 서버를 활용하여 조사하고, 비교하고, 개선 아이디어를 포착해 봅시다!

1. Codespace에서 열려있는 파일을 모두 닫습니다. 불필요한 컨텍스트를 줄이는 데 도움이 됩니다.

1. **Copilot Chat** 패널이 열려있고 **Agent** 모드가 선택되어 있는지 확인합니다. MCP 서버 도구도 여전히 사용 가능한지 확인합니다.

1. Copilot에게 이 프로젝트와 유사한 GitHub 프로젝트를 검색하도록 요청합니다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Search for any other repositories for organizing extra curricular activities
   > ```

1. MCP 도구가 필요한 경우 Copilot이 권한을 요청할 수 있습니다. **요청을 확인**하고 필요 시 수정한 후 **Continue**를 클릭합니다.

   <img width="250" alt="request permission dialog" src="https://github.com/user-attachments/assets/229473af-c206-47a4-b356-943b9c9bd946" />

1. Copilot에게 프로젝트 중 하나를 설명해 달라고 요청합니다. 마음에 드는 것을 찾을 때까지 탐색합니다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please look at the code for the 3rd option and give me a detailed description of the features.
   > ```

1. Copilot을 사용하여 비교하고 개선 아이디어를 생성합니다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please compare these features to our project. Which would be new?
   > ```

1. 좋습니다! Copilot이 이런 아이디어를 이슈로 저장하도록 합시다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I like it. Let's create issues for these in my repository.
   > ```

1. Copilot이 저장소에 이슈를 생성할 권한을 요청합니다. 각 새 이슈에 대해 **Continue**를 클릭합니다. 주의: 실행 전에 **요청을 확인**하세요.

   <img width="250" alt="request permission dialog" src="https://github.com/user-attachments/assets/52635294-950a-4168-b71e-498eb769f3af" />

1. 조사가 끝났으니, 컨텍스트를 지우기 위해 이 채팅 세션을 종료합시다. **Copilot Chat** 패널 상단에서 **New Chat** 아이콘(플러스 기호)을 클릭합니다.

1. 새 이슈가 생성되면 Mona가 이미 작업을 확인하고 있을 것입니다. 잠시 기다리며 댓글을 확인하세요. 진행 상황과 다음 레슨이 표시됩니다.

> [!NOTE]
> Model Context Protocol (MCP) 환경은 빠르게 발전하고 있습니다. [공식 GitHub MCP 서버](https://github.com/github/github-mcp-server)를 포함한 많은 서버가 활발히 개발 중이며 안정적인 API와 완전한 동등성을 갖추지 못한 상태입니다.
"""

# Step 3
files[".github/steps/3-step.md"] = r"""## Step 3: 에이전트 모드와 GitHub MCP 서버로 이슈 해결하기

유사 프로젝트를 조사하고 잠재적 협업 기회를 찾은 것, 잘 하셨습니다.
과외 활동 정리에 도움이 되는 새 아이디어를 찾았을 뿐만 아니라, 그것도 빠르게 해냈습니다.

이제 MCP 서버의 도구와 Copilot을 사용하여 약간의 분류 작업을 하고 일을 처리합시다.

### :keyboard: 활동: 중요한 이슈 쉽게 구현하기

이슈 백로그가 쌓이고 있습니다. 하나를 처리해 봅시다. 어떤 이슈가 먼저 주의를 받아야 할까요?

1. **Copilot Chat** 패널이 열려있고 **Agent** 모드가 선택되어 있는지 확인합니다. MCP 서버 도구도 여전히 사용 가능한지 확인합니다.

1. Copilot에게 이 저장소의 열린 이슈에 대해 물어봅니다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > How many open issues are there on my repository?
   > ```

   > 🪧 **참고:** List Issues 도구가 적절한 매개변수로 호출되는지 확인하세요.

1. Copilot에게 중요한 이슈를 요약해 달라고 요청합니다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Oh no. That's too many for me! Please get the list of issues,
   > review the descriptions and comments, and pick the top 3 most important.
   > ```

   <details>
   <summary> <b> 💡 팁:</b> 도구 사용 사전 승인</summary><br/>

   Copilot이 도구를 자주 사용하면, 나머지 대화 세션 동안 사전에 권한을 부여할 수 있습니다.

   <img width="350" src="https://github.com/user-attachments/assets/d741191e-4d98-489d-92d2-f1069fd6c34e"/>

   </details>

1. 제안된 이슈를 검토합니다. Copilot이 구체적인 추천을 하지 않았다면, 결과를 좁히기 위해 피드백을 제공해 보세요.

1. 목록을 좁힌 후, Copilot에게 이슈를 구현하도록 요청합니다. **Mona는 변경사항이 작동하는지가 아니라, 시도가 이루어졌는지만 평가합니다.**

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Let's do the first one. Follow these steps:
   > 1. Checkout a new local branch for making our changes.
   > 2. Make the changes then confirm with me that they look correct.
   > 3. Push the changes and create a pull request.
   > ```

   > ⚠️ **경고:** Copilot이 수행하려는 작업을 항상 확인하세요. 특히 MCP 서버가 제공하는 외부 기능은 실행 취소 옵션이 없을 수 있습니다.

1. 풀 리퀘스트가 생성되면 Mona가 작업 확인을 시작합니다. 잠시 기다리며 댓글을 확인하세요. 진행 상황과 다음 단계가 표시됩니다!

<details>
<summary>문제가 있나요?</summary><br/>

- 도구가 요청되지 않으면 MCP 구성이 올바른지 확인하세요.
- Copilot이 결과를 가져올 수 없다면, 이 Codespace의 토큰 또는 적절한 권한이 있는 개인 접근 토큰(PAT)을 사용하고 있는지 확인하세요. 기본적으로 사용 중인 Codespace 토큰은 이 저장소에만 접근할 수 있습니다.

</details>
"""

# Step 4
files[".github/steps/4-step.md"] = r"""## Step 4: AI 생성 코드 검증하기

이슈를 구현해 주셨습니다! 과외 활동 사이트가 날마다 좋아지고 있습니다! 💚

GitHub Copilot과 같은 AI 어시스턴트가 생산성을 크게 향상시킬 수 있지만, 생성 여부에 관계없이 모든 작업을 검토하고 검증하는 것은 **_여러분_**의 책임이라는 것을 기억하는 것이 중요합니다.

> [!tip]
> 실제 프로젝트에서 많은 팀이 [GitHub Actions](https://github.com/features/actions)를 사용하여 자동화된 테스트를 설정합니다.

### :keyboard: 활동: AI 솔루션 검토 및 머지하기

1. Copilot이 만든 새 풀 리퀘스트를 새 탭에서 엽니다.

   [![풀 리퀘스트 확인하기](https://img.shields.io/badge/-풀%20리퀘스트%20열기-1f883d?logo=github)]({{pull_request_url}})

   > ✨ **보너스:** Copilot 구독에서 제공한다면, 특수 버전의 Copilot을 사용하여 [변경사항을 리뷰](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review?tool=webui)할 수도 있습니다.

1. 변경사항을 검토합니다. 만족스러우면 풀 리퀘스트를 머지합니다.

1. VS Code와 활성 **Copilot Chat** 세션으로 돌아갑니다.

   > 🚨 **중요:** 이전에 Done을 클릭하여 이전 대화로 돌아가야 한다면, Copilot Chat 패널 상단의 **Show Chats** 버튼을 사용하여 복원하세요.

1. Copilot에게 방금 완료한 이슈에 댓글을 추가하고, 댓글과 아이디어에 감사하라고 요청합니다.

   > ![Static Badge](https://img.shields.io/badge/-프롬프트-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Add a closing comment to the issue we just finished. Provide a 1 sentence description
   > of the implemented solution and thank the commenters for their ideas and feedback.
   > ```

   <details>
   <summary>문제가 있나요? 🤷</summary><br/>

   확인할 사항들

   - MCP 서버가 여전히 실행 중인가요?
   - MCP 서버 호출에 전달되는 정보를 확인하세요 - Copilot이 올바른 저장소를 사용하고 있나요?
   - Copilot이 버그 리포트에 댓글을 달았나요?
   </details>

1. 댓글이 생성되면 Mona가 작업 확인을 시작합니다. 잠시 기다려 피드백이나 최종 리뷰를 확인하세요. 잘 하셨습니다! 모두 완료되었습니다! 🎉
"""

# Review
files[".github/steps/x-review.md"] = r"""## 리뷰

_축하합니다, 이 실습을 완료하고 MCP와 GitHub Copilot을 통합하는 방법을 배웠습니다!_

<img src=https://octodex.github.com/images/collabocats.jpg alt=celebrate width=300 align=right>

배운 내용을 정리하면:

- **MCP 서버 구성**: GitHub MCP 서버를 설정하고 Copilot에 연결하기
- **MCP를 활용한 에이전트 모드**: 자연어를 사용하여 MCP 도구를 통해 외부 서비스와 상호작용하기
- **GitHub 저장소 조사**: MCP 기능을 사용하여 유사한 프로젝트를 검색하고 분석하기
- **이슈 관리 및 구현**: Copilot을 통해 GitHub 이슈를 분류, 생성, 관리하고, Copilot이 이슈를 해결하도록 하기

### 다음 단계

더 배우거나 참여하려면 다음 리소스를 확인하세요:

- [다른 GitHub Skills 실습 수강하기](https://learn.github.com/skills).
- [Model Context Protocol](https://modelcontextprotocol.io/introduction)에 대해 더 알아보기
- [GitHub MCP 레지스트리](https://github.com/mcp)를 탐색하고 다른 서버를 시도해 보기!
"""

# Issue files - these stay mostly English since they are app content, but translate titles/comments
files[".github/steps/1-step-issues/bug/school-pride.md"] = r"""# 학교 자부심 표현 부족

웹사이트가 파란색인데, 우리 학교 색은 흰색과 라임 그린입니다. 이것 좀 고쳐주세요.

또한, 왜 마스코트가 페이지에 하나도 없나요?
https://octodex.github.com/ 에서 다양한 옵션을 사용해 주세요.

아, 하나 더, 배경에 다양한 Git 스타일 브랜치 라인이 천천히 애니메이션되면 멋질 것 같습니다! 쉽죠?
"""

files[".github/steps/1-step-issues/enhancement/activities-file.md"] = r"""# 활동 변경이 어려움

선생님들이 프로그램을 수정하면 망가뜨릴까봐 두려워합니다. 활동 목록을 Python 파일에서 별도의 `activities.json` 파일로 옮겨주세요.
"""

files[".github/steps/1-step-issues/enhancement/add-filters.md"] = r"""# 필터 추가

활동에 순서가 없는 것 같습니다. 이것 좀 고쳐주세요.

제 아이디어입니다. 활동 카드 위에 툴바로 넣으면 좋겠습니다.

- 필터를 추가해주세요. 예를 들어 카테고리별로. 필요하면 JSON에 필드를 추가하세요.
- 정렬 옵션을 추가해주세요. 예를 들어 이름이나 시간별로. 필요하면 날짜 필드를 추가하되 시간의 텍스트 설명 버전은 유지하세요.
- 자유 텍스트 검색을 추가해주세요.

물론, 데스크톱과 폰에서 여전히 보기 좋게 해주세요.

----- COMMENTS -----
정말 유용할 거예요. 목록이 더 길어지기 전에 미리 해두면 좋겠습니다.
해봅시다! 도와드리고 싶어요. 방금 코딩 수업을 들었거든요. 🤓
"""

files[".github/steps/1-step-issues/enhancement/admin-mode.md"] = r"""# 관리자 모드

## 문제

학생들이 활동에 자리를 확보하기 위해 서로를 제거하고 있습니다.

## 권장 솔루션

오른쪽 상단에 사용자 아이콘을 추가합니다. 클릭하면 로그인 버튼이 나타납니다. 로그인 버튼을 클릭하면 사용자명과 비밀번호를 입력하는 창이 표시됩니다.
- 선생님(로그인한 사용자)만 학생을 활동에 등록 및 등록 해제할 수 있습니다.

- 학생(로그인하지 않은 사용자)은 누가 등록되어 있는지 볼 수만 있습니다.

- 계정 관리 페이지는 필요하지 않습니다. 선생님에게 비밀번호가 할당됩니다.

## 맥락

아직 데이터베이스가 없으므로, 선생님 사용자명과 비밀번호를 백엔드에서 확인하는 `json` 파일에 저장해 주세요.
"""

files[".github/steps/1-step-issues/enhancement/missing-activity.md"] = r"""# 🚨 누락된 활동: GitHub Skills

교장 선생님이 발표한 GitHub Skills 활동이 학교 활동 등록 페이지에 없습니다.

어제 조회에서 교장 선생님이 학생들에게 실용적인 코딩과 협업 기술을 가르치기 위한 GitHub와의 새 파트너십을 발표했습니다. 하지만 이 활동에 등록하려고 하면 웹사이트에서 찾을 수 없습니다.

다른 활동들은 보이는데, 접근 권한은 있는 것 같습니다.

- ✅ 체스 클럽
- ✅ 프로그래밍 수업
- ✅ 체육 수업

## ⏱️ 일정

발표에서 이번 주 말까지 등록이 마감된다고 했기 때문에 시급합니다. 많은 학생들이 참여를 원합니다. 이것은 대학 지원에 도움이 될 [GitHub 인증 프로그램](https://resources.github.com/learn/certifications/)의 첫 번째 파트입니다.

## 💡 예상 결과

GitHub Skills 활동이 시스템에 추가되어 다른 활동처럼 등록할 수 있어야 합니다.

Hewbie C.
11학년 학생
"""

files[".github/steps/1-step-issues/enhancement/prettier-interface.md"] = r"""# 더 예쁜 인터페이스

활동이 많아지면서 왼쪽 목록이 너무 길어 탐색이 어렵습니다. 그리고 추가 대화상자가 활동에서 너무 멀리 있습니다.

- 카드를 하단으로 이동해주세요.

- 등록 양식을 제거하고 각 활동 카드에 "학생 등록" 버튼으로 교체해주세요.

- 데스크톱과 폰에서 보기 좋게 해주세요.

----- COMMENTS -----
이 아이디어에 동의합니다. 제 활동을 찾기가 어렵습니다.
100% 지지합니다. 좋은 아이디어입니다! 업데이트가 기대됩니다.
태블릿도 잊지 마세요.
"""

for path, content in files.items():
    full_path = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.lstrip("\n"))
    print(f"Wrote {path}")

print("Done! All step and issue files translated.")
