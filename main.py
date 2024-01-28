def check_hemoglobin_level(gender, hemoglobin):
    if gender.lower() == 'female':
        if 117 <= hemoglobin <= 155:
            return "Normal hemoglobin level for adult females."
        elif hemoglobin < 117:
            return "Low hemoglobin level for adult females."
        else:
            return "High hemoglobin level for adult females."
    elif gender.lower() == 'male':
        if 134 <= hemoglobin <= 167:
            return "Normal hemoglobin level for adult males."
        elif hemoglobin < 134:
            return "Low hemoglobin level for adult males."
        else:
            return "High hemoglobin level for adult males."
    else:
        return "Invalid gender input. Please enter 'male' or 'female'."

def main():
    gender = input("Enter your biological gender (male/female): ")
    hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

    result = check_hemoglobin_level(gender, hemoglobin)
    print(result)

if __name__ == "__main__":
    main()

