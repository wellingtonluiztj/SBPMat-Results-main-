set term gif animate # delay 10      -->  [1:100]  1-rapido y 2-lento
set output "anim-gnu.gif"  

N = 100

do for [i=0:N:1] \
{

  reset
  set pm3d map
  set size ratio -1
  set cbrange [0.00 to 2.00]
  unset xtics
  unset ytics
  unset colorbox
  unset border
  unset key
  set xrange[0:250]
  set yrange[0:90]
  set palette defined(0.00 "cyan" , 1.00 "black" , 2.00 "dark-gray")
  set contour base
  set cntrparam level discrete 0,0.5
  #set arrow 1 from  9,1,0 to  9,129,0 nohead lt 0 lw 1.5 lc rgb 'red' front
  #set arrow 2 from 137,1,0 to 137,129,0 nohead lt 0 lw 1.5 lc rgb 'red' front
  if (i>=0 && i<=100) \
  {
    if (i>=0 && i<=9) \
    {
      set label 1 sprintf('t =   %d',i) at 64,-10
      splot sprintf('gnu_output/RES-00%d.dat',i) u 1:2:($8==0 ? $4 : $8+1)
    }
    else \
    {
      if (i>=10 && i<=99) \
      {
        set label 1 sprintf('t =  %d',i) at 64,-10
        splot sprintf('gnu_output/RES-0%d.dat',i) u 1:2:($8==0 ? $4 : $8+1)
      }
      else \
      {
        set label 1 sprintf('t = %d',i) at 64,-10
        splot sprintf('gnu_output/RES-%d.dat',i) u 1:2:($8==0 ? $4 : $8+1)
      }
    }
  }
  else \
  {
    if (i<0) \
    {
      set label 1 sprintf('t =   %d',0) at 64,-10
      splot sprintf('gnu_output/RES-00%d.dat',0) u 1:2:($8==0 ? $4 : $8+1)
    }
    else \
    {
      set label 1 sprintf('t = %d',N) at 64,-10
      splot sprintf('gnu_output/RES-%d.dat',N) u 1:2:($8==0 ? $4 : $8+1)
    } 
  }
  unset label 1
  
  #if (i==0) {pause mouse "Click on the figure to start the animation"}
  #pause 0.1
  print i
  
}

print ''
print 'finish, press enter'

#pause -1
exit
