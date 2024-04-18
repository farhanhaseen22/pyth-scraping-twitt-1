def wage_calc(cw, hw, mlwh):

    current_wage = cw
    hours_worked = hw
    totalPay = current_wage * hours_worked
    print(f"{current_wage} * {hours_worked}")
    print(f"Total Money Earned: {totalPay}")

    if mlwh != 0:
        minutes_last_worked_hour = mlwh
        temp = 60 * (minutes_last_worked_hour / 100)
        print(f"Total Minutes of the Last Worked Hour: {temp}")

        # minutesOfTheLastWorkedHour = MOTLWH
        moneyFromMOTLWH = (current_wage * temp) / 60
        print(
            f"Money Earned from the Minutes of the Last Worked Hour: {round(moneyFromMOTLWH, 2)}"
        )
    else:
        moneyFromMOTLWH = 0
    
    finalTotalPay = totalPay + moneyFromMOTLWH

    print(f"Total Money Earned after considering everything: {finalTotalPay}")

    print(
        f"Total Money Earned after considering everything: {round(finalTotalPay, 2)}"
    )
    
    return round(finalTotalPay, 2)

if __name__ == "__main__":
    # cw, hw, mlwh
    wc1 = wage_calc(16.20, 12, 0)
    wc2 = wage_calc(16.88, 44, 0)
    wc3 = wage_calc(16.22, 7, 0)
    wc4 = wage_calc(16.22, 3, 0)
    
    vacation_pay = 43.97
    
    totsies = round(wc1+wc2+wc3+wc4+vacation_pay, 2)
    print(f"Adding every wages, we get: {totsies}")

