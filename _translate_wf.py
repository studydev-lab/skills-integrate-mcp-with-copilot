#!/usr/bin/env python3
"""Translate workflow files for integrate-mcp-with-copilot."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
WF_DIR = os.path.join(BASE, ".github", "workflows")

for filename in sorted(os.listdir(WF_DIR)):
    if not filename.endswith('.yml'):
        continue

    filepath = os.path.join(WF_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change exercise-toolkit references (various versions)
    content = re.sub(
        r'skills/exercise-toolkit/\.github/workflows/([\w-]+\.yml)@v[\d.]+',
        r'skills-kr/exercise-toolkit/.github/workflows/\1@kr-v0.6.0',
        content
    )
    content = content.replace(
        'repository: skills/exercise-toolkit',
        'repository: skills-kr/exercise-toolkit'
    )
    content = re.sub(
        r'ref: v0\.\d+\.\d+',
        'ref: kr-v0.6.0',
        content
    )

    # 2. Translate exercise title
    content = content.replace(
        'exercise-title: "Integrate MCP with Copilot"',
        'exercise-title: "MCP와 GitHub Copilot 통합하기"'
    )
    content = content.replace(
        'exercise-title: "Integrate MCP with GitHub Copilot"',
        'exercise-title: "MCP와 GitHub Copilot 통합하기"'
    )

    # 3. Translate intro-message
    content = content.replace(
        'intro-message: "This exercise will help you learn how to expand GitHub Copilot\'s capabilities with Model Context Protocol (MCP)."',
        'intro-message: "이 실습은 Model Context Protocol (MCP)을 사용하여 GitHub Copilot의 기능을 확장하는 방법을 배우는 데 도움이 됩니다."'
    )

    # 4. Translate workflow names
    name_translations = {
        'name: Step 0 # Start Exercise': 'name: Step 0 # 실습 시작',
        'name: Step 1\n': 'name: Step 1 # MCP 소개 및 환경 설정\n',
        'name: Step 2\n': 'name: Step 2 # 에이전트 모드와 MCP 서버\n',
        'name: Step 3\n': 'name: Step 3 # MCP로 이슈 해결하기\n',
        'name: Step 4\n': 'name: Step 4 # AI 코드 검증 및 마무리\n',
    }
    for eng, kor in name_translations.items():
        content = content.replace(eng, kor)

    # 5. Translate job names
    job_translations = {
        'name: Start Exercise': 'name: 실습 시작',
        'name: Post next step content': 'name: 다음 단계 안내',
        'name: Find Exercise Issue': 'name: 실습 이슈 찾기',
        'name: Check step work': 'name: 작업 확인',
        'name: Create issues': 'name: 이슈 생성',
        'name: Post review content': 'name: 리뷰 내용 게시',
        'name: Finish Exercise': 'name: 실습 완료',
    }
    for eng, kor in job_translations.items():
        content = content.replace(eng, kor)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")

print("Done! All workflow files updated.")
