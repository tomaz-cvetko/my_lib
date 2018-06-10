void setup()
{
  size(800, 600);
  print("hello");
  print(cos(0));
}    
    
float t = 0.0;
float omega = 0.5;
float k0 = PI/width;
//float k2 = k1+0.01;
float k = k0;
int N = 50;

void simpleSum(int N)
{
  float odmik = 0;
  stroke(255);
  noFill();
  beginShape();
  for(int i = 0; i < width; ++i){
    odmik = 0;
    k = k0;
    point(i, height/2);
    for(int j = 0; j < N; j++){
      odmik += height/(2*N)*(cos(k*(i-width/2) - omega*t));
      k += 0.0005;
    }
    vertex(i, odmik+height/2);
  }
  endShape();
}

void probability(float N)
{
  float amplitude = 0;
  stroke(255);
  noFill();
  beginShape();
  for(int i = -width/2; i < width/2; ++i){
    /* Za vsako koordinato i (=x) poracunaj vsoto verjetnosti */
    amplitude = 0;
    k = k0;
    for(int j = 0; j < N; ++j){
      //float jth = cos(k*i - omega*t);
      double jth = 1/(2*N)*(cos(k*i - omega*t));
      //print(jth);
      //print("\n");
      //break;
      amplitude += jth;
      k += 0.0005;
    }
    vertex(i + width/2, height/2*(1.8 - 6*amplitude*amplitude));
    
  }
  endShape();
}

void draw()
{
  
  background(0);
  //simpleSum(N);
  probability(N);
  t += 0.05;
}