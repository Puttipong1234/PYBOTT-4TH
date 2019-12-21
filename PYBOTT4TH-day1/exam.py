def car_timer(in_hr,in_min,out_hr,out_min):
    #ใส่ค่าเวลาสี่ค่า รีเทิน จำนวนเงินที่ต้องจ่าย
    #find difference btw in and out 

    diff_hr = int(out_hr) - int(in_hr) #ออกตอน 8 เข้าตอน 7

    diff_hr_to_min = diff_hr*60

    diff_min = int(out_min) - int(in_min) #ออกตอน 10  เข้าตอน 40  เป็นลบ

    total_diff_min = diff_hr_to_min + diff_min

    if total_diff_min <= 15:
        return 0 #free

    elif 15 < total_diff_min <= 3*60:
        calculate_hr = int(total_diff_min/60) * 10
        if total_diff_min%60:
            calculate_hr += 10
        
        return calculate_hr

    elif 3*60 < total_diff_min <= 6*60:
        pay_0_3 = 3*10
        total_diff_min -= 3*60
        calculate_hr = int(total_diff_min/60) * 20
        if total_diff_min%60:
            calculate_hr += 20
        
        return calculate_hr + pay_0_3

    else:
        return 200




