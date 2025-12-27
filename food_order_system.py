{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red0\green0\blue0;\red202\green202\blue202;
\red212\green212\blue212;\red194\green126\blue101;\red70\green137\blue204;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\csgray\c0\c0;\cssrgb\c83137\c83137\c83137;
\cssrgb\c86275\c86275\c86275;\cssrgb\c80784\c56863\c47059;\cssrgb\c33725\c61176\c83922;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 italian_food = \strokec5 [\strokec6 "Pasta Bolognese"\strokec5 ,\strokec4  \strokec6 "Pepperoni Pizza"\strokec5 ,\strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec6 "Margherita Pizza"\strokec5 ,\strokec4  \strokec6 "Lasagna"\strokec5 ]\strokec4 \
\
indian_food = \strokec5 [\strokec6 "Curry"\strokec5 ,\strokec4  \strokec6 "Chutney"\strokec5 ,\strokec4  \strokec6 "Samosa"\strokec5 ,\strokec4  \strokec6 "Naan"\strokec5 ]\strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec7 def\strokec4  find_meal\strokec5 (\strokec4 name\strokec5 ,\strokec4  menu\strokec5 ):\strokec4 \
  \strokec7 if\strokec4  name \strokec7 in\strokec4  menu\strokec5 :\strokec4 \
    \strokec7 return\strokec4  name\
  \strokec7 else\strokec5 :\strokec4 \
    \strokec7 return\strokec4  \strokec7 None\strokec4 \
\
\strokec7 def\strokec4  is_meal_ready\strokec5 ():\strokec4 \
  \strokec7 pass\strokec4 \
\
\strokec7 def\strokec4  select_meal\strokec5 (\strokec4 name\strokec5 ,\strokec4  food_type\strokec5 ):\strokec4 \
  \strokec7 if\strokec4  food_type == \strokec6 "Italian"\strokec5 :\strokec4 \
    \strokec7 return\strokec4  find_meal\strokec5 (\strokec4 name\strokec5 ,\strokec4  italian_food\strokec5 )\strokec4 \
  \strokec7 elif\strokec4  food_type == \strokec6 "Indian"\strokec5 :\strokec4 \
    \strokec7 return\strokec4  find_meal\strokec5 (\strokec4 name\strokec5 ,\strokec4  indian_food\strokec5 )\strokec4 \
  \strokec7 else\strokec5 :\strokec4 \
    \strokec7 return\strokec4  \strokec7 None\strokec4 \
\
  \
\strokec7 def\strokec4  create_summary\strokec5 (\strokec4 name\strokec5 ,\strokec4  amount\strokec5 ,\strokec4  food_type\strokec5 ):\strokec4 \
  order = select_meal\strokec5 (\strokec4 name\strokec5 ,\strokec4  food_type\strokec5 )\strokec4 \
  \strokec7 if\strokec4  order\strokec5 :\strokec4 \
    \strokec7 return\strokec4  f\strokec6 "You ordered \{amount\} \{name\}"\strokec4 \
  \strokec7 else\strokec5 :\strokec4 \
    \strokec7 return\strokec4  \strokec6 "Meal not found"\strokec4 \
\
\strokec7 def\strokec4  display_available_meals\strokec5 (\strokec4 food_type\strokec5 ):\strokec4 \
  \strokec7 if\strokec4  food_type == \strokec6 "Italian"\strokec5 :\strokec4 \
    \strokec7 for\strokec4  meal \strokec7 in\strokec4  italian_food\strokec5 :\strokec4 \
      \strokec7 print\strokec5 (\strokec4 meal\strokec5 )\strokec4 \
  \strokec7 elif\strokec4  food_type == \strokec6 "Indian"\strokec5 :\strokec4 \
    \strokec7 print\strokec5 (\strokec6 "Available Indian Meals: "\strokec5 )\strokec4 \
    \strokec7 for\strokec4  meal \strokec7 in\strokec4  indian_food\strokec5 :\strokec4 \
      \strokec7 print\strokec5 (\strokec4 meal\strokec5 )\strokec4 \
  \strokec7 else\strokec5 :\strokec4 \
    \strokec7 print\strokec5 (\strokec6 "Invalid food type"\strokec5 )\strokec4 \
\
\strokec7 print\strokec5 (\strokec6 "Welcome to the Food Order System!"\strokec5 )\strokec4 \
\
type_input = \strokec7 input\strokec5 (\strokec6 "Do you want Italian or Indian? "\strokec5 )\strokec4 \
display_available_meals\strokec5 (\strokec4 type_input\strokec5 )\strokec4 \
name_input = \strokec7 input\strokec5 (\strokec6 "Please enter a meal: "\strokec5 )\strokec4 \
amount_input = \strokec7 int\strokec5 (\strokec7 input\strokec5 (\strokec6 "Please enter quantity: "\strokec5 ))\strokec4 \
\
result = create_summary\strokec5 (\strokec4 name_input\strokec5 ,\strokec4  amount_input\strokec5 ,\strokec4  type_input\strokec5 )\strokec4 \
\strokec7 print\strokec5 (\strokec4 result\strokec5 )\strokec4 \
}