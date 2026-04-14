# MCP와 GitHub Copilot 통합하기

_GitHub Copilot에 더 많은 도구를 제공하여 개발 워크플로우의 기능을 확장하는 방법을 배워보세요. 1시간 이내로 완료할 수 있습니다!_

## 환영합니다

- **대상**: AI 지원 워크플로우를 향상시키려는 개발자, GitHub Copilot 사용자, AI 매니아.
- **배울 내용**: MCP 기초, GitHub MCP 서버 설정, Copilot 에이전트 모드와의 통합을 소개합니다.
- **만들 것**: GitHub Copilot을 사용하여 이슈를 관리하면서 Mergington 고등학교의 과외 활동 웹사이트를 업그레이드하는 혼합 개발 워크플로우를 만듭니다.
- **사전 요구사항**: [Copilot 시작하기](https://github.com/skills-kr/getting-started-with-github-copilot) 실습
- **소요 시간**: 이 실습은 1시간 이내에 완료할 수 있습니다.

이 실습에서 다음을 수행합니다:

1. GitHub MCP 서버를 GitHub Copilot과 통합합니다.
2. Copilot에게 유사한 프로젝트를 조사하고 이슈를 생성하도록 위임합니다.
3. Copilot에게 중요한 이슈를 찾아 아이디어에서 풀 리퀘스트까지 구현하도록 요청합니다.
4. 최근 종료된 이슈에 댓글을 추가합니다.

### 이 실습을 시작하는 방법

> [!IMPORTANT]
> 이 실습은 [GitHub Copilot](https://github.com/features/copilot)에 대한 기본 지식을 전제로 합니다. 익숙하지 않다면 [Copilot 시작하기](https://github.com/skills-kr/getting-started-with-github-copilot) 실습을 먼저 수강하세요.

실습을 자신의 계정으로 복사한 후, 좋아하는 Octocat(Mona)에게 **약 20초** 정도 첫 번째 레슨을 준비할 시간을 주고 **페이지를 새로고침**하세요.

[![](https://img.shields.io/badge/실습%20복사-%E2%86%92-1f883d?style=for-the-badge&logo=github&labelColor=197935)](https://github.com/new?template_owner=skills-kr&template_name=integrate-mcp-with-copilot&owner=%40me&name=skills-integrate-mcp-with-copilot&description=Exercise:+Integrate+Model+Context+Protocol+with+GitHub+Copilot&visibility=public)

<details>
<summary>문제가 있나요? 🤷</summary><br/>

실습을 복사할 때 다음 설정을 권장합니다:

- 소유자(owner)는 개인 계정 또는 저장소를 호스팅할 조직을 선택하세요.

- 공개 저장소로 만드는 것을 권장합니다. 비공개 저장소는 Actions 사용 시간을 소모합니다.

20초 후에도 실습이 준비되지 않았다면, [Actions](../../actions) 탭을 확인해 주세요.

- 작업이 실행 중인지 확인하세요. 때로는 조금 더 시간이 걸릴 수 있습니다.

- 페이지에 실패한 작업이 표시되면, 이슈를 제출해 주세요. 버그를 발견했네요! 🐛

</details>

> **참고**: 이 실습은 [skills/integrate-mcp-with-copilot](https://github.com/skills/integrate-mcp-with-copilot)를 기반으로 한글화하고, [🏆 GitHub Skills Workshop Dashboard](https://github-skills.studydev.com)와 연계되어 있습니다.

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
