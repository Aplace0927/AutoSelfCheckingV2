import ascInstance as inst

if __name__ == "__main__":
    Ps = [
        #['이름','생일YYMMDD','비번']
    ]

    Sinfo = ['XX고등학교','고등학교','서울']    #[학교명, 학교급, 지역]

    for Pinfo in Ps:
        Student = inst.StudentAutoCheckInstance(Pinfo,Sinfo)
        Student.run()