class Time_str:

    def zamiana_czasu(self,time):
        time_str = time.split(":")
        if len(time) > 1:

            if len(time_str[0]) == 1:
                time_str[0] = "0"+time_str[0]
                time_limit = time_str[0]

            if len(time_str[1]) == 1:
                time_str[1] = "0"+time_str[1]
            time1 = time_str[0]
            time2 = time_str[1]
            if int(time1) >23 and len(time_str[0]) > 1:
                time_str[0] = "23"
            if int(time2) >59 and len(time_str[1]) > 1:
                time_str[1] = "59"
        final_string=":".join(time_str)
        print(final_string)



