## Step 3: 에이전트 모드와 GitHub MCP 서버로 이슈 해결하기

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
