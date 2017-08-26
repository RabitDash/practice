var canvas=document.getElementById('canvas')
var cxt=canvas.getContext('2d')
var img=new Image()
img.src="test.png"
var x = 0
var y = 0
img.onload = function(){
  cxt.drawImage(img,x,y)
}
var leftDown = false
var rightDown = false
window.addEventListener('keydown',function(event){
  console.log(event.key)
  var k = event.key
  if (k == 'a'){
    leftDown = true
  }else if (k == 'd') {
    rightDown = true
  }

})
window.addEventListener('keyup',function(event){
  console.log(event.key)
  var k = event.key
  if (k == 'a'){
    leftDown = false
  }else if (k == 'd') {
    rightDown = false
  }

})
var update = function(){
  cxt.clearRect(0, 0, canvas.width, canvas.height)
  cxt.drawImage(img, x, y)
}
setInterval(function(){
    if (leftDown){
      x -= 5
    } else if (rightDown) {
      x += 5
    }
    update()
},1000/30)
