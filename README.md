Optimizing for the the maximum allowed Voltage that produces a 100 degree temperature within a multi-morph thermal resonator.

Given a range of 0.06 [V] to 0.1 [V], the python script output is:

```
Temp       Volts
76.855151879       0.06
80.708667963       0.062
84.688528538       0.064
88.794734649       0.066
93.027283968       0.068
97.386179385       0.07
101.87141917       0.072
106.48300374       0.074
111.22093346       0.076
116.08520669       0.078
121.07582614       0.080
126.19278981       0.082
131.43609832       0.084
136.8057517        0.086
142.30174962       0.088
147.92409239       0.090
153.67278006       0.092
159.54781246       0.094
165.54918884       0.096
171.67691161       0.098
177.93062348       0.100

The maximum Voltage was  0.072 [V] which caused a temperature of:  101.87141917 [degrees C]
```

# FlexPDE Models and Plots:
![bending_img](https://lh3.googleusercontent.com/Kc0A2bCLbQO6d6FM1Zz0osTpne-q4DAFi4D0_oa39y65vx5wsfoNXo6dxN8LE9kwbR4WXH9kNHc30GOC0r230aRRi6LY0TV6NurSjIFZ6EXVRrIxbeytBQlPnoUaYIcbWJLsWtpHbYVecVKiR3-wZD8jDIOW3F4cP4708RLBGbOBInnZadPG_EaxmwGy4tM0BONo_i4wb96oTQ9sB2WtnEMF5sqlhq9rTCnE-Ca6BVKizQwiLexvYH-tuqxbDQUPoqW7ThyYlDrfj8a8W2aP-0uP0dM5ARWlKQeEJbtXdV87jgu7o_uD7T9CLl1RmLmTROhgZitNPsqqAAncnIx16n4xoJ6Tg7XMjCVK4WD6Wr8oFiydVm5uBhZ2bI8L6CkRRpkc_QtnUhisVgQ4ZCWic0Ydhirxae3f1L275AzkpQ7j_hEOHfqFfKpO7pvDZ5Gt0q_wvOYSvKxGQTuKVgBu-CLY7YphK59-8-ZDVCgMUFZJa2f_2ecm7D4t0FX94gKmQ3eZjJ1k98f50BbWOFQL0butWyyI5lvLPd62jjcTHs5jytj3pMRB2scOgKqtNyTxO5ghXC7Pskevs4UmEe4buzorOOzB4Qe6y1T3CKF0AMIhtteTPe-L_lXtfSoUob3R-fCMZmCGEUygIzOEf9VbFNx_RyFre0qkMu6z8R-cDoI5VddxzlWRFvuIaANr=w799-h809-no)
Multimorph bending

![tipDisplacement](https://lh3.googleusercontent.com/44tlwo-g5j2bfDRuYGYKhylBw7r2ALXcNTXm4D5D6oQ6g4re0CMg1KoVc2uDT3ccKn0Nei3o7RFYdQnlKDRvytl-g2_kDgRiW6lva4OsWaUm8rxv_KuonvHMCT09xHMVVsahs_Jy_5FedMpZ3Rnc787lw_3t6iHgI2WQ_F0m8-i664GzwVq5wGFa6VwSJUExW7HJqwrQLLgVfNTBdLDocINjvxT8XiOI8NpkwC-CAUrdXBcIfr3-mZ_EyenKnrmB9dQE8HpHczAuYJFBucWyO18s59juFIE1j3Y8q6VSqMSQmVHf5QX8sw7Y-aiCwBJNqaeT205E9C7FfD8Lznyz-6a3BVyNHwr0UcM-6y5f6mpjEoQg5fOHR9LxjcLrD3NwHpcCl-N5PRf8-8cD1xqQjn85MjqcmaJOV3za6uR8jJa2lvFyl45M036Twd6d9MQNu5STV76PHUeumkxHoSIR2ry5NxaGuWvoJ7lDSw-iC1ipSrvpWymoW56r3NyIcMm42SrqVql94CnGTF7cUC6TIityP6O90nnXUphJlLW1MhBgUM5V8P0rntpg4XBQ_NhMR0vR-nOQlWm3Y1ypDydGcXhSwRsjO56aKFxv2dh3ytbnq1oIN8Z3gUJTJZmd1_YKgupSTqvbKJKBZd6R2SAQ77uGWLWQwLXeHXtGCXLPeqX3SpJ-BtZ7edEQjkHE=w795-h819-no)
Tip Displacement in y-direction

![Temp](https://lh3.googleusercontent.com/W7eyPpH2ysliwKeLYRZMJezEBsvwUSt3IgZuJ3Qw2J_1_yqZjcDO6qKJjQsvMMprT5k5dH8D4z1C1vu_XxaQdnVwspcjIAGYmj6LcYWmCU8qxct8vbZdkr9wAcaEVlIpldyDygH1q_ddTHCuyFCdY7EEoMsJy3WcaIZ5JHdQ1qVNWtQTkAEJePr1YUkPmQj1drIcJlfXLtML6n9Z_plih89nHKQBI7Eo4dbIVvPEzfcW_gQPIYuu-ZyuTqXUyOR8cnmOyyITd75be561P6IMeRbx6RDL0Hg7tSqGPeVn8CIJaS4KYzU0wLubjLbQ_JBOkTTeQ1JkgAqlCd8CIF77VcAB05PSPTU3Bj4f8g9hXYjW7VPw6NpRh6f0J9jyJvCPuGoQRBcS4UEmJTX_y-D880DjsML8FK2mPQQsO5JENmUdPPCtyg2NKTAfURkabNzDGeiqXjrcBWwsHfLcNL81bNwNZsJ6YwiLm-AhMcBjsdED9dPI8t4Ba9oTS5AfgpL5CToXjWc6NCgoy3CT8jc6Rt_DbmtsfFrV5QAmUoIFtwx3tkf1UoRBX0niX0brzSGGGA2rhZv0zCQa_o4O1AK5AuP8eKysxB7xTIV6y29_bJuY72zbuWjg25OgjFGiMidzSiOEC6SPuXxVVoWTFoLF3T_B2uwMy0xZgw3M8b130_hF57nGyK3LMTJ7S3PX=w1180-h825-no)
Temperature Contour

# Other Plots
Running the file `MultimorphResonatorSim.pde` will produce additional contours, vector fields, and plots such as:
* Voltage 
* Current Density
* Heat Flux Density
* Electric Field
