void
function(canvas) {
  var grdColors = ["#b3b3b3"];
  var dotsColor = "black";
  var dotsAmount = 50;
  var bigDotsAmount = 0;
  var speedLimit = .3;
  var lineLength = 200;




  var lnLngthSqrd = lineLength * lineLength;
  var cnv = canvas;
  var ctx = cnv.getContext("2d");
  var dotsList = [];
  var bigDotsList = [];
  cnv.width = window.innerWidth;
  cnv.height = window.innerHeight;


  var realSizeHeight = window.innerHeight;
  var initWindowHeight = window.innerHeight;

  var grd = ctx.createLinearGradient(0, 0, 0, cnv.height);

  init();


  function init() {


    //Initializing gradient
    for (var i = 0; i < grdColors.length; i++) {
      console.log(i + "x" + grdColors[i]);
      grd.addColorStop(i * (1 / grdColors.length), grdColors[i]);
    }

    for (var i = 0; i < dotsAmount; i++) {
      dotsList.push(new dot(rand(0, cnv.width, false), rand(0, cnv.height, false), rand(2, 3, true)));

    }
    for (var i = 0; i < bigDotsAmount; i++) {
      bigDotsList.push(new dot(rand(0, cnv.width, false), rand(0, cnv.height, false), rand(2, 40, true)));

    }
    for (var i = 0; i < dotsAmount; i++) {
      for (var j = 0; j < dotsAmount; j++) {
        var distanceSquared = (dotsList[i].coordinates[0] - dotsList[j].coordinates[0]) * (dotsList[i].coordinates[0] - dotsList[j].coordinates[0]) + (dotsList[i].coordinates[1] - dotsList[j].coordinates[1]) * (dotsList[i].coordinates[1] - dotsList[j].coordinates[1]);
        if (Math.abs(distanceSquared) < lnLngthSqrd) {
          dotsList[i].friends.push(dotsList[j]);
        }
      }
    }


    ctx.fillStyle = grd;
    ctx.fillRect(0, 0, cnv.width, cnv.height);
    setInterval(frame, 25);


  }

  function frame() {

    cnv.height = initWindowHeight - document.body.scrollTop * 2;




    if (parseInt(cnv.height) < 25) {
      cnv.height = 25;
    }
    cnv.style.width = "100%";
    ctx.fillStyle = grd;
    //ctx.fillStyle="red";
    ctx.fillRect(0, 0, cnv.width, cnv.height);
    for (var i = 0; i < dotsAmount; i++) {
      dotsList[i].move();

      //console.log(dotsList[i].coordinates[1] +"x"+dotsList[i].coordinates[0]);
      dotsList[i].draw(0.2);

      for (var j = 0; j < dotsAmount; j++) {
        var distanceSquared = (dotsList[i].coordinates[0] - dotsList[j].coordinates[0]) * (dotsList[i].coordinates[0] - dotsList[j].coordinates[0]) + (dotsList[i].coordinates[1] - dotsList[j].coordinates[1]) * (dotsList[i].coordinates[1] - dotsList[j].coordinates[1]);
        if (Math.abs(distanceSquared) < lnLngthSqrd) {
          ctx.globalAlpha = 0.02 * (lnLngthSqrd / Math.abs(distanceSquared));
          ctx.beginPath();
          ctx.strokeStyle = dotsColor;
          ctx.moveTo(dotsList[i].coordinates[0], dotsList[i].coordinates[1]);
          ctx.lineTo(dotsList[j].coordinates[0], dotsList[j].coordinates[1]);
          ctx.stroke();
          ctx.globalAlpha = 1;
        }
      }



    }
    for (var i = 0; i < bigDotsAmount; i++) {
      bigDotsList[i].move();

      //console.log(dotsList[i].coordinates[1] +"x"+dotsList[i].coordinates[0]);
      ctx.shadowBlur = 10;
      ctx.shadowColor = dotsColor;
      bigDotsList[i].draw(0.02);
      ctx.shadowBlur = 0;
    }

  }

  function dot(x, y, size) {
    this.coordinates = [x, y];
    this.size = size;
    this.vects = [0, 0];
    this.friends = [];

    this.move = function() {

      this.vects[0] += rand(-0.1, 0.2, false);
      this.vects[1] += rand(-0.1, 0.2, false);
      if (this.vects[0] > speedLimit) {
        this.vects[0] -= 0.1;
      }
      if (this.vects[0] < -speedLimit) {
        this.vects[0] += 0.1;
      }
      if (this.vects[1] > speedLimit) {
        this.vects[1] -= 0.1;
      }
      if (this.vects[1] < -speedLimit) {
        this.vects[1] += 0.1;
      }


      if (this.coordinates[0] < 0) {
        this.coordinates[0] = 0;
      }
      if (this.coordinates[0] > cnv.width) {
        this.coordinates[0] = cnv.width;
      }
      if (this.coordinates[1] > realSizeHeight) {
        this.coordinates[1] = realSizeHeight;
      }
      if (this.coordinates[1] < 0) {
        this.coordinates[1] = 0;
      }
      this.coordinates[0] += this.vects[0];
      this.coordinates[1] += this.vects[1];
    }
    this.draw = function(opacity) {


      ctx.globalAlpha = 1;
      //ctx.shadowBlur=2;
      //ctx.shadowColor=dotsColor;
      ctx.beginPath();
      ctx.fillStyle = dotsColor;

      ctx.arc(this.coordinates[0], this.coordinates[1], this.size, 0, 2 * Math.PI);
      ctx.closePath();
      ctx.fill();
      ctx.globalAlpha = 1;
      //ctx.shadowBlur=0;
    }
  }


  function rand(min, max, round) {
    switch (round) {
      case true:
        return Math.round(Math.random() * max + min);
      case false:
        return Math.random() * max + min;
    }
  }
}(document.getElementById('cnv'))
