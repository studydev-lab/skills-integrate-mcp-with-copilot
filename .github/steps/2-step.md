## Step 2: 에이전트 모드와 GitHub용 MCP 서버

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
