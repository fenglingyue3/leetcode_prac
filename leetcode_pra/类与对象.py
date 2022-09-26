class clock:
    clock_id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)


clock1 = clock()
clock1.clock_id = '001001'
clock1.price = 35.5
print(f'闹钟{clock1.clock_id}的价格为：{clock1.price}')
clock1.ring()