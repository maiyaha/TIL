# GIT 명령어

- git status :
    깃 상태 확인(stage 올려진 상태 파악)
- git init :
    깃 폴더 생성(하위 폴더 전부 제어)
- git add .
    stage에 올리기(추가)
    온점 또는 * 은 dir 내 파일 전체 애드
- cd :
    파일 경로 변경(상위 directory로)
- cd 폴더명 :
    해당 폴더(디렉토리)로 이동
- git remote :
    현재 깃의 원격 정보 확인
- touch 파일명.확장자 :
    dir 내에 파일 생성
- git commit -m '파일명' :
    stage에 추가된 파일을 커밋(확정), -m을통애 해당 커밋의 버전명 메모
- git checkout 브랜치명 
  git switch 브랜치명 :
    해당 브랜치로 이동
    git checkout -b 브랜치명 : -b로 브랜치 생성과 동시에 이동
- mkdir 폴더명 :
    해당 폴더(dir) 생성
- git branch :
    현재 branch 목록 확인
- git log :
    현재 깃의 커밋 이력(log) 확인
- git rm 파일명.확장자 :
    파일 삭제
- git rm -rf :
    파일 강제 삭제, rm으로 지울 수 없는 것도 강제로 지움, 하위 디렉토리까지 지울 수 있음
- git remote add origin https:// ... .git :
    원격 저장소(레포지토리)에 연결
- git push :
    파일 전체 업로드
- git push -u origin 브랜치명 :
    해당 브랜치의 파일들(커밋 완료된) 업로드
- git pull origin 브랜치 :
    해당 브랜치의 파일을 다운로드(당겨옴)
- git clone 주소 :
    깃헙에 있는 깃을 로컬로 클로닝
- pwd :
    현재 경로(위치) 확인

# 특수 파일

- redme.md :
    마크다운 언어로 작성되는 md파일,
    설명 등을 담음
- .gitignore : 
    폴더 내의 파일 중 깃헙 등 push시에 일부 파일을 무시(업로드되지 않도록)할 수 있도록 함

## 유데미, 노마드, 인프런 등

## 최근 master보다 main 브랜치를 권장
