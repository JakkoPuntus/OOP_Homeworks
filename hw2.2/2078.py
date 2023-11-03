def calculate_scores(frames):
    min_score = 0
    max_score = 0
    i = 0

    for frame in range(10):
        if frames[i] == 10:  # Страйк
            min_score += 10
            max_score += 10 + frames[i + 1] + frames[i + 2]
            i += 1
        elif frames[i] + frames[i + 1] == 10:  # Спэр
            min_score += 10
            max_score += 10 + frames[i + 2]
            i += 2
        else:
            min_score += frames[i] + frames[i + 1]
            max_score += frames[i] + frames[i + 1]
            i += 2

        if i >= 9:
            break

    return min_score, max_score

# Считываем результаты бросков
frames = list(map(int, input().split()))

min_score, max_score = calculate_scores(frames)
print(min_score, max_score)
