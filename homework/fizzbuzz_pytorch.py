import torch
import numpy as np

'''
3的倍数说fizz,5的倍数说buzz,15的倍数fizzbuzz
'''


# 人工定义的规则代码
def fizz_buzz_encode(i):
    if i % 15 == 0:
        return 3
    elif i % 5 == 0:
        return 2
    elif i % 3 == 0:
        return 1
    else:
        return 0


def fizz_buzz_decode(i, prediction):
    return [str(i), "fizz", "buzz", "fizzbuzz"][prediction]


def helper(i):
    print(fizz_buzz_decode(i, fizz_buzz_encode(i)))


for i in range(1, 16):
    # helper(i) #暂时注释用不上

    NUM_DIGITS = 10


def binary_encode(i, num_digits):
    return np.array([i >> d & 1 for d in range(num_digits)][::-1])


trX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(101, 2 ** NUM_DIGITS)])
trY = torch.LongTensor([fizz_buzz_encode(i) for i in range(101, 2 ** NUM_DIGITS)])
print(trX.shape)

'''
用pytorch定义模型
'''
NUM_HIDDEN = 100
model = torch.nn.Sequential(
    torch.nn.Linear(NUM_DIGITS, NUM_HIDDEN),
    torch.nn.ReLU(),
    torch.nn.Linear(NUM_HIDDEN, 4)  # 4 logits, after softmax, we get a probability distribution
)
if torch.cuda.is_available():
    model = model.cuda()

loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)

BATH_SIZE = 128
for epoch in range(10000):
    for start in range(0, len(trX), BATH_SIZE):
        end = start + BATH_SIZE
        batchX = trX[start:end]
        batchY = trY[start:end]

        if torch.cuda.is_available():
            batchX = batchX.cuda()
            batchY = batchY.cuda()

        y_pred = model(batchX)  # forward
        loss = loss_fn(y_pred, batchY)

        print("epoch", epoch, loss.item())

        optimizer.zero_grad()
        loss.backward()  # back pass
        optimizer.step()  # gradient descent

testX = torch.Tensor([binary_encode(i, NUM_DIGITS) for i in range(1, 101)])
if torch.cuda.is_available():
    testX = testX.cuda()
with torch.no_grad():
    testY = model(testX)

predictions = zip(range(1, 101), testY.max(1)[1].cpu().data.tolist())

print([fizz_buzz_decode(i, x) for i, x in predictions])