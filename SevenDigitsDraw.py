import turtle as tu
import time as ti
def drawGap():  #绘制数码管间隔
    tu.penup()
    tu.fd(5)
def drawline(draw): #绘制单段-数码管
    drawGap()
    tu.pendown() if draw else tu.penup()
    tu.fd(40)
    drawGap()
    tu.right(90)
def drawDigit(digit):   #根据数字绘制七段数码管
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    tu.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    tu.left(180)
    tu.penup()  #为绘制后续数字确定位置
    tu.fd(20)   #为绘制后续数字确定位置
def drawDate(date): #data为日期，格式为 ‘%Y-%m=%d+’
    tu.pencolor('red')
    for i in date:
        if i == '-':
            tu.write('年',font=('Arial',36,'normal'))
            tu.pencolor('green')
            tu.fd(50)
        elif i == '=':
            tu.write('月',font=('Arial',36,'normal'))
            tu.pencolor('blue')
            tu.fd(50)
        elif i == '+':
            tu.write('日',font=('Arial',36,'normal'))
        else:
             drawDigit(eval(i))
def main():
    tu.setup(950,450)
    tu.penup()
    tu.fd(-300)
    tu.pensize(5)
    drawDate(ti.strftime('%Y-%m=%d+',ti.gmtime()))
    tu.hideturtle()
    tu.done()
main()

