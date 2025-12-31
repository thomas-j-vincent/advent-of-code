with open("Day3Input.txt", "r") as file:
    text = file.read().strip()

text = text.replace("\n", ",")
numbers = [v.strip('"') for v in text.split(",")]
#numbers = [98765431111111,811111111111119,234234234234278, 818181911112111]
total = 0

for i in numbers:
    digits = [int(ch) for ch in str(i)]
    removes = 88  #len(digits) - 12

    result = []
    print(result)

    for d in digits:
        while result and removes > 0 and result[-1] < d:
            result.pop()
            removes -= 1
        result.append(d)

    # If we still need to remove digits, remove from the end
    result = result[:12]

    temporaryTotal = ''.join(map(str, result))
    total += int(temporaryTotal)
    print(f"final{result}")
print(f"total:{total}")
