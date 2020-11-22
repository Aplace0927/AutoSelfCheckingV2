# ASC v2
#### Auto Self-Checking System v2.0.0
---
**INTRODUCTION**
새로워진 자가진단 사이트에 호환하는 새로운 자가진단 시스템, ASC 2.0

**POLICY**

본 프로그램을 이용하여 발생하는 **모든 법적 책임은 사용자 본인에게 있습니다.**

**HOW TO USE**
ascMain.py에 있는 Ps list 에 **[이름,생년월일,비밀번호]** 형태의 list로 개인정보를 추가해 주시면 됩니다.

```Python
import ascInstance as inst

if __name__ == "__main__":
    Ps = [
        ["홍길동","YYMMDD","1234"] #[이름,생일,비밀번호]
    ]
    
```



---

**ERROR HAPPENS**

에러가 발생할 시 대부분의 원인은 사용자 개인정보 입력의 오류이거나 로딩 중에 발생하는 오류입니다.

이를 해결하기 위해,

* 다시 한 번 개인정보의 입력이 정확한지 확인해 보세요.

* ascInstance.py에 있는 변수를 조금 키워 보세요.

  * `MAX_WAIT_TIME`은 webdriver이 최대로 기다리는 시간을 조절합니다.

  * `SLEEP_TIME`은 비밀번호 입력 중 추가적으로 기다리는 시간을 조절합니다.

  * 기본값은 `MAX_WAIT_TIME = 5`, `SLEEP_TIME = 1` 입니다. (단위 : 초)

    ```python
    import ascXp as xp
    import ascConst as con
    import time
    
    MAX_WAIT_TIME = 5
    SLEEP_TIME = 1
    
    class StudentAutoCheckInstance:
        def __init__(self,PersonalInfo,SchoolInfo):
            ...
    ```

    

    
