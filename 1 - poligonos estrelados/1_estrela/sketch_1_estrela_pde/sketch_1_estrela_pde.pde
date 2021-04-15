class C {
 
  private float x, y, raio;

  C(float x, float y, float raio)
  {
     this.x = x;
     this.y = y;
     this.raio = raio;
  }
  
  void desenha()
  {
    ellipseMode(CENTER);
    fill(255,255,0);
    circle(this.x, this.y, this.raio);
  }
  
}

C c = null;

void setup()
{
  size(800,600);
  rectMode(CENTER);
  ellipseMode(CENTER);
  frameRate(20);
}

void draw() 
{
  background(200);
  int margem = 20;
  float points = round(map(mouseY, 0, width, 5, 5));
  float angle = TWO_PI/points;
  float r1 = (width/2) - margem;
  float r2 = r1 * map(mouseY, 0, width, 0.3, 0);
  translate(width/2, height/2);
  beginShape();
  for(int i = 0; i < points * 2; i++){
    if( i % 2 == 0){
      float x = r1 * cos(i*angle) / 2;
      float y = r1 * sin(i*angle) / 2;
    }
    else{  
      float x = r2 * cos(i*angle) / 2;
      float y = r2 * sin(i*angle) / 2;
      vertex(x,y);
    }
  }
  endShape(CLOSE);
}
