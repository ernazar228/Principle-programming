from db import save_result, get_top_scores, get_personal_best

save_result("player1", 150, 3)

print("TOP 10:")
print(get_top_scores())

print("Best score:")
print(get_personal_best("player1"))