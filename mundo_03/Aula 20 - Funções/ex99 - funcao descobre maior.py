'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
import os
os.system('cls||clear')

from time import sleep

def maior(* num):
    print(f'Os numeros digitados foram: {num}, o maior é: {max(num)}',flush=True)
    sleep(0.5)
    

#Programa Principal
maior(2,5,6,3,8)
maior(6,8,0,7,9,3,2,1)
maior(1,2)
maior(6)