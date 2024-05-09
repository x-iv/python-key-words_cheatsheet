weather: tuple[str, int] = 'rainy', 6

match weather:
    case 'rainy', severity if severity <= 5:
        print(f'huh ({severity})')
    case 'rainy', severity if severity > 5:
        print(f'huuuh ({severity})')
    case 'cloudy', severity:
        print('hehehe')
    case _:
        print('hahahahahhahahahahah')

