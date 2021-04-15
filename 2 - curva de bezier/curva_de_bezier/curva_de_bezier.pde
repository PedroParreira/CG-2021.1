void setup(){
  size(800,800);
}

void draw(){
  background(100);
  noFill();
  bezier(0, 800, 720, 720, 80, 80, 800, 0);
  fill(255);
  int steps = 800;
  float i;
  i = mouseX;
  float t = i / float(steps);
  float x = bezierPoint(0, 720, 80, 800, t);
  float y = bezierPoint(800, 720, 80, 0, t);
  ellipse(x, y, 5, 5);
}
