
fiftk = 80000//50000
tenk = (80000%50000)//10000
fivek = (((80000%50000)%10000)//5000)

print("5만원권",fiftk,"장 ","만원권",tenk,"장 ","5천원권 ",fivek,"장 냅니다.")
print("거스름돈은",(fiftk*50000+tenk*10000+fivek*5000)-78000,"원")