// // #include <gtest/gtest.h>

// // #include "model.h"

// const double kEpsilon_ = 1e-6;

// TEST(smartcalc_2_basic, case_1) {
//   const char *str = "sin(1+15)*14^1-36/2.4";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -19.0306464333;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_2) {
//   const char *str = "2+2*2/2-2";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 2;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_3) {
//   const char *str = "(1-(-1+((-1)+(1))+(+1)-(-1)+1-(+1)))*17";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_4) {
//   const char *str = "sin(0)+cos(0)+tan(0)+asin(0)+acos(0)+atan(0)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 2.5707963;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_5) {
//   const char *str = "9mod(2)*3^2-sqrt(9)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 6;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_6) {
//   const char *str = "ln(1)+log(100)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 2;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_7) {
//   const char *str = "(x+x)^x-x-(-x)+x+(+x)*x";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 2);
//   double reference = 22;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_8) {
//   const char *str = "4.5/1.5";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 3;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_9) {
//   const char *str = "2^(-3)+14";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 14.125;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_10) {
//   const char *str = "(((2^(-3)+14)*3+2)-1*4)-(-4)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 44.375;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_11) {
//   const char *str = "2*(3-3)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_12) {
//   const char *str = "sqrt(x)-1/2*sin(x^2-2-4+13)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 3);
//   double reference = 1.8760024659;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_13) {
//   const char *str = "sin(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 0.8414709848;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_14) {
//   const char *str = "sin(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 0);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_15) {
//   const char *str = "sin(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, -1);
//   double reference = -0.8414709848;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_16) {
//   const char *str = "cos(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 0.54030230586;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_17) {
//   const char *str = "cos(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 0);
//   double reference = 1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_18) {
//   const char *str = "cos(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, -1);
//   double reference = 0.54030230586;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_19) {
//   const char *str = "tan(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, -1);
//   double reference = -1.55740772465;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_20) {
//   const char *str = "tan(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 0);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_21) {
//   const char *str = "tan(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 1.55740772465;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_22) {
//   const char *str = "tan(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 1.55740772465;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_23) {
//   const char *str = "asin(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 1.57079633;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_24) {
//   const char *str = "asin(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 0);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_25) {
//   const char *str = "asin(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, -1);
//   double reference = -1.57079633;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_26) {
//   const char *str = "acos(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_27) {
//   const char *str = "acos(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 0);
//   double reference = 1.57079633;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_28) {
//   const char *str = "acos(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, -1);
//   double reference = 3.14159265;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_29) {
//   const char *str = "atan(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 0.785398163;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_30) {
//   const char *str = "atan(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 0);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_31) {
//   const char *str = "atan(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, -1);
//   double reference = -0.785398163;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_32) {
//   const char *str = "sqrt(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 15);
//   double reference = 3.87298334621;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_33) {
//   const char *str = "sqrt(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 335);
//   double reference = 18.3030052177;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_34) {
//   const char *str = "5mod(3)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 2;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_35) {
//   const char *str = "71mod(12)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 11;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_36) {
//   const char *str = "71mod(12)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 11;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_37) {
//   const char *str = "2mod(2)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_38) {
//   const char *str = "(-5)mod(-3)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -2;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_39) {
//   const char *str = "(-71)mod(-12)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -11;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_40) {
//   const char *str = "(-2)mod(-2)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_41) {
//   const char *str = "(-5)mod(3)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_42) {
//   const char *str = "(-71)mod(12)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_43) {
//   const char *str = "(-2)mod(2)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_44) {
//   const char *str = "(5)mod(-3)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_45) {
//   const char *str = "71mod(-12)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_46) {
//   const char *str = "2mod(-2)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_47) {
//   const char *str = "2.13mod(-21.1)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -18.97;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_48) {
//   const char *str = "(-2.13)mod(21.1)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 18.97;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_49) {
//   const char *str = "ln(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_50) {
//   const char *str = "ln(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 10);
//   double reference = 2.30258509299;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_51) {
//   const char *str = "ln(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 264);
//   double reference = 5.57594910315;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_52) {
//   const char *str = "log(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 1);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_53) {
//   const char *str = "log(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 10);
//   double reference = 1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_54) {
//   const char *str = "log(x)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 264);
//   double reference = 2.42160392687;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_55) {
//   const char *str = "2^(-13)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0.00012207031;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_56) {
//   const char *str = "2^13";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 8192;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_57) {
//   const char *str = "(-2)^13";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -8192;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_58) {
//   const char *str = "(-2)^(-13)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -0.00012207031;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_59) {
//   const char *str = "(-3)^(-2)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0.11111111111;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2_basic, case_60) {
//   const char *str = "(-2)^(-13)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = -0.00012207031;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_1) {
//   const char *str = "3+7";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 3 + 7;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_2) {
//   const char *str = "2/(3+2)*5";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   EXPECT_EQ(my_res, 2);
// }

// TEST(smartcalc_2, case_3) {
//   const char *str = "10+10*10";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   EXPECT_EQ(my_res, 110);
// }

// TEST(smartcalc_2, case_4) {
//   const char *str = "((1.0)-2.0-((-3.0)-(4.0)))-5.0-(-6.0)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   EXPECT_EQ(my_res, 7);
// }

// TEST(smartcalc_2, case_5) {
//   const char *str = "5.0-(4.0)-x+((x)-x-((x*(-1.0))))";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 3);
//   double reference = 1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_6) {
//   const char *str = "(x*(-1.0))-((x*(-1.0)))";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 3);
//   double reference = 0;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_7) {
//   const char *str = "(-5.0)mod(-3.0)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   EXPECT_EQ(my_res, -2);
// }

// TEST(smartcalc_2, case_8) {
//   const char *str = "3+4*2/(1-5)^2";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   EXPECT_EQ(my_res, 3.5);
// }

// TEST(smartcalc_2, case_9) {
//   const char *str = "sqrt(x)-1/2*sin(x^2-2)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 2.7);
//   double reference = 2.0620524126;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_10) {
//   const char *str = "-(-(-(-3+7)))";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   EXPECT_EQ(my_res, -4);
// }

// TEST(smartcalc_2, case_11) {
//   const char *str = "3+2+1*4^sin(3-1)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 8.52737474297;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_12) {
//   const char *str = "(-5.0)mod(-3.0)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   EXPECT_EQ(my_res, -2);
// }

// TEST(smartcalc_2, case_13) {
//   const char *str = "2^3^1";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 8;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_14) {
//   const char *str = "1.0/2.0*(2.0-1.0)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 0.5;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_15) {
//   const char *str = "(1.0+2.0)*((3.0-4.0)+1.0+(5.0-6.0+7.0))";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 18;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_16) {
//   const char *str = "1.1+2.0+(3.0*4.0)+(5.0+6.8)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str);
//   double reference = 26.9;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_17) {
//   const char *str = "8.0^(1.0/((x*(-1.0))))";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 6);
//   double reference = 0.70710678118;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_18) {
//   const char *str = "log(x)+log(-2.0+4.0)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 17);
//   double reference = 1.53147891704;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_19) {
//   const char *str = "cos(x)^2.0+sin(x)^2.0";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 17);
//   double reference = 1;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(smartcalc_2, case_20) {
//   const char *str = "-1.0*sin(cos(tan((x*(-1.0))^2.0)^3.0)^4.0)";
//   s21::Model my_model;
//   double my_res = my_model.GetResult(str, 17);
//   double reference = -0.84147098443;
//   ASSERT_NEAR(reference, my_res, kEpsilon_);
// }

// TEST(exception, case_1) {
//   const char *str = "3+7-";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_2) {
//   const char *str = "3+sin(e+7)";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_3) {
//   const char *str = ".3+17";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_4) {
//   const char *str = "(1+2)17";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_5) {
//   const char *str = "(1+2)x";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_6) {
//   const char *str = "(1++2)";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_7) {
//   const char *str = "*3";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_8) {
//   const char *str = "3(2)";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_9) {
//   const char *str = "3*mod";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_10) {
//   const char *str = "3*)";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// TEST(exception, case_11) {
//   const char *str = "3sin(x)";
//   s21::Model my_model;
//   EXPECT_THROW(my_model.GetResult(str), std::exception);
// }

// int main(int argc, char **argv) {
//   testing::InitGoogleTest(&argc, argv);
//   return RUN_ALL_TESTS();
// }
