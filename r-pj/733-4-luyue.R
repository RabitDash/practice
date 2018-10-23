# 一、基本操作

## 1
x<-seq(-4*pi,4*pi,0.1)
y<-sin(x)
plot(x,y,type="o")

## 2
t<-rnorm(40)
View(t)
t<-sort(t,decreasing=T)
which.max(t)
max(t)
mean(t)
median(t)
boxplot(t)

## 3
A<-matrix(c(1,3,3,3,3,2,3,3,3,3,3,3,3,3,3,4),ncol=4,byrow=T)
det(A)
nrow(A)
ncol(A)
B<-t(A)
A%*%B

## 4
C<-diag(1:4)
View(C)

## 5
b<-1:4
x<-solve(A,b)
View(x)

## 6
iris.1<-iris[iris[1]>5,]
View(iris.1)


# 二、数据题目

## 1
white<-read.csv("white.csv", sep=";")
typeof(white)
nrow(white)

## 2
unique(white["quality"])

## 3
colnames(white)[12]<-"yf"
boxplot(white[1],white["yf"])


# 三
f<-function(x){
	if(x > 1)
	{
		2 * x^2 + 1
	}
	else
	{
		3 * x
	}
}
f(1)+2*f(3)
x<-seq(-5,5,0.1)
plot(x,sapply(x, f),main = "the plot of f",type = "o",col="red")


# 四
matrix(sapply(1:10000, function(i){0.4^abs(i%%100-i%/%100-1)}),nrow=100)

