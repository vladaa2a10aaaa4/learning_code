current_day = float(input())
current_weight = float(input())
max_weight_loss = 0.2 * current_day
target_weight = 100.0 - max_weight_loss
if current_weight <= target_weight:
    status = "Все идет по плану"
else:
    status = "Что-то пошло не так"
print(f"""{status}
#{int(current_day)} ДЕНЬ: ТЕКУЩИЙ ВЕС = {current_weight:.1f} кг, ЦЕЛЬ по ВЕСУ = {target_weight:.1f} кг""".strip())
