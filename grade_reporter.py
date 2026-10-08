scores = [72, 45, 90, 61, 38]

passes = 0
fails = 0
total = 0

for score in scores:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Score: {score} -> Grade: {grade}")
    
    if score >= 50:
        passes += 1
    else:
        fails += 1
        
    total += score

average = round(total / len(scores), 1)

print(f"Passed: {passes}")
print(f"Failed: {fails}")
print(f"Average: {average}")