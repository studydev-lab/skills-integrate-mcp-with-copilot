## Step 4: AI 생성 코드 검증하기

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
