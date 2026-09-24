from kivy.core.window import Window

Window.fullscreen = True
Window.clearcolor = (0, 0, 0, 1)

import random
import json
import math
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock

__version__ = "1.0.0"

class MathsQuizApp(App):
    def build(self):
        self.main_layout = FloatLayout()
        self.quiz_finished = False

        self.matrix_layout = FloatLayout()
        self.main_layout.add_widget(self.matrix_layout)

        self.matrix_labels = []

        for i in range(45):
            label = Label(
                text=random.choice(["0", "1"]),
                font_size=random.randint(14, 26),
                color=(0, 1, 0, random.uniform(0.2, 0.9)),
                size_hint=(None, None),
                size=(30, 30),
                pos=(random.randint(0, Window.width), random.randint(0, Window.height))
            )

            self.matrix_layout.add_widget(label)
            self.matrix_labels.append(label)

        Clock.schedule_interval(self.matrix_fall, 1 / 30)

        self.page_layout = FloatLayout()
        self.main_layout.add_widget(self.page_layout)

        Window.bind(on_key_down=self.on_key_down)

        self.score = 0
        self.load_stats()
        self.home_page()

        return self.main_layout
 
    def matrix_fall(self, dt):
        for label in self.matrix_labels:
            label.y -= random.randint(2, 7)

            if label.top < 0:
                label.x = random.randint(0, int(Window.width))
                label.y = Window.height

                label.text = random.choice(
                    ["0", "1"]
                )

                label.color = (
                    0,
                    1,
                    0,
                    random.uniform(0.2, 0.9)
                )
 
    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        if key == 27:
            self.stop_timer()
            self.home_page()
            return True

        if key in (120, 88):
            self.stop_timer()
            self.stop()
            return True

        if key in (13, 271):
            if hasattr(self, "answer") and self.answer.focus:
                self.enter_pressed(self.answer)
                return True

        return False
 
    def home_page(self):
        self.page_layout.clear_widgets()
    
        layout = BoxLayout(
            orientation="vertical",
            padding=(30, 5, 30, 30),
            spacing=20,
            size_hint=(None, None),
            width=400,
            height=500,
            pos_hint={"center_x": 0.5, "top": 1}
            )
    
        title = Label(
            text="MATHS QUIZ",
            font_size=35,
            size_hint_y=None,
            height=80,
            color="white"
        )
    
        Lessons = Button(
            text="Lessons",
            font_size=20,
            size_hint_y=None,
            height=50
        )
    
        Mt_quiz = Button(
            text="Maths Quiz",
            font_size=20,
            size_hint_y=None,
            height=50
        )

        Mt_quiz.bind(on_press=self.Maths_Quiz)
    
        QS = Label(
            text=f"Quizzes Passed: {self.passed_quizzes}\nQuizzes Failed: {self.failed_quizzes}",
            font_size=20,
            color="white",
            size_hint_y=None,
            height=60
        )
        
        Leaderboard = Button(
            text="Leaderboard",
            font_size=20,
            size_hint_y=None,
            height=50
        )
        
        text = Label(
            text = "Press  'x'  key to leave the app.",
            color = "red",
            height = 50,
            font_size = 20
        )

        layout.add_widget(title)
        layout.add_widget(Lessons)
        layout.add_widget(Mt_quiz)
        layout.add_widget(Leaderboard)
        layout.add_widget(QS)
        layout.add_widget(text)

        Leaderboard.bind(on_press=self.show_leaderboard)
        Lessons.bind(on_press=self.Lesson)

        self.page_layout.add_widget(layout)

    def Lesson(self, instance):
        def hide_buttons():
            buttons = [
                Root, Square, Cube, Area, Polygon,
                Fractions, Decimals, Percentages, Integers,
                Factors, Multiples, Prime_Numbers, LCM, HCF,
                Ratio_Missing, Ratio_Simplest, Proportion, Average, 
                Profit_Loss, Simple_Interest, Speed, Distance, Time,
                Algebra, Linear_Equations, Exponents,
                Order_of_Operations, Perimeter, Volume,
                Triangles, Quadrilaterals, Circles, Angles,
                Coordinates, Probability, Statistics, Patterns,
                Sequences, Cos, Sec, Cosec, Tan, Cot, Sin , 
                Natural_Sum, Odd_Sum, Even_Sum,
                Cube_Root_Trick, Square_Identities,
                Calculus, Pythagoras,
                Circle_Perimeter, Circle_Area, 
                Rational_Numbers, Quadratic_Equations,
                Congruence_of_Triangles, Laws_of_Exponents,
                Algebraic_Identities, Factorization_Algebraic_Expressions,
                Polynomials, Arithmetic_Progressions,
                Euclidean_Geometry, Similarity_of_Triangles,
                Areas_Parallelograms_Triangles, Circle_Chords_Arcs,
                Surface_Area_Cubes_Cuboids, Surface_Area_Cylinders_Cones,
                Volume_Cylinders_Cones_Spheres, Herons_Formula,
                Trigonometric_Ratios, Trigonometric_Identities,
                Heights_and_Distances, Statistics_Mean_Median_Mode,
                Grouped_Data_Frequency_Tables, Probability_Compound_Events,
                Permutations_Combinations, Profit_Loss_Discount,
                Compound_Interest, Tax_Financial_Mathematics,
                Speed_Distance_Relative_Speed, Time_and_Work,
                Pipes_and_Cisterns, Ratio_Proportion_Word_Problems,
                Mixtures_Alligation, Unitary_Method,
                Percentage_Applications, HCF_LCM_Word_Problems,
                Decimal_Fraction_Word_Problems, Rational_Algebraic_Expressions,
                Linear_Inequalities, Graphs_Linear_Equations,
                Systems_Linear_Equations, Symmetry_Transformations,
                Construction_Geometric_Figures, Angle_Properties_Theorems,
                Polygons_Interior_Angles, Mathematical_Reasoning,
                Data_Interpretation, Number_Theory_Divisibility,
                Mathematical_Word_Problems,
                Back, Back2
            ]

            for button in buttons:
                if button.parent:
                    lesson_layout.remove_widget(button)


        def show_lesson(explanation):
            hide_buttons()
            lesson_layout.add_widget(explanation)
            lesson_layout.add_widget(Back2)
            lesson_layout.add_widget(Back)

        self.page_layout.clear_widgets()

        scroll = ScrollView(
            size_hint=(1, 1),
            do_scroll_x=False,
            do_scroll_y=True
        )

        lesson_layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=30,
            size_hint_y=None
        )

        lesson_layout.bind(
            minimum_height=lesson_layout.setter("height")
        )


        Root = Button(
            text="Root",
            font_size=16,
            size_hint_y=None,
            height = 45
        )

        Square = Button(
            text="Square",
            font_size=16,
            size_hint_y=None,
            height = 45
        )

        Cube = Button(
            text="Cube",
            font_size=16,
            size_hint_y=None,
            height = 45
        )

        Area = Button(
            text="Area",
            font_size=16,
            size_hint_y=None,
            height = 45
        )

        Polygon = Button(
            text="Polygon",
            font_size=16,
            size_hint_y=None,
            height = 45
        )

        Fractions = Button(
            text="Fractions",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Decimals = Button(
            text="Decimals",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Percentages = Button(
            text="Percentages",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Integers = Button(
            text="Integers",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Factors = Button(
            text="Factors",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Multiples = Button(
            text="Multiples",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Prime_Numbers = Button(
            text="Prime Numbers",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        LCM = Button(
            text="LCM",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        HCF = Button(
            text="HCF",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Ratio_Simplest = Button(
            text="Ratio - Simplest Form",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Ratio_Missing = Button(
            text="Ratio - Missing Part",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Proportion = Button(
            text="Proportion",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Average = Button(
            text="Average",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Profit_Loss = Button(
            text="Profit & Loss",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Simple_Interest = Button(
            text="Simple Interest",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Speed = Button(
            text="Speed",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Distance = Button(
            text="Distance",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Time = Button(
            text="Time",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Algebra = Button(
            text="Algebra",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Linear_Equations = Button(
            text="Linear Equations",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Exponents = Button(
            text="Exponents",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Order_of_Operations = Button(
            text="Order of Operations",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Perimeter = Button(
            text="Perimeter",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Volume = Button(
            text="Volume",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Triangles = Button(
            text="Triangles",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Quadrilaterals = Button(
            text="Quadrilaterals",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Circles = Button(
            text="Circles",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Angles = Button(
            text="Angles",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Coordinates = Button(
            text="Coordinates",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Probability = Button(
            text="Probability",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Statistics = Button(
            text="Statistics",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Patterns = Button(
            text="Patterns",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Sequences = Button(
            text="Sequences",
            font_size=16,
            size_hint_y=None,
            height=45
        )
        
        Sin = Button(
            text="Sine (sin)",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Cos = Button(
            text="Cosine (cos)",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Tan = Button(
            text="Tangent (tan)",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Cosec = Button(
            text="Cosecant (cosec)",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Sec = Button(
            text="Secant (sec)",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Cot = Button(
            text="Cotangent (cot)",
            font_size=16,
            size_hint_y=None,
            height=45
        )
        
        Natural_Sum = Button(
            text="Sum of Natural Numbers",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Odd_Sum = Button(
            text="Sum of Odd Numbers",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Even_Sum = Button(
            text="Sum of Even Numbers",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Cube_Root_Trick = Button(
            text="Cube Root Trick",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Square_Identities = Button(
            text="Algebraic Square Identities",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Calculus = Button(
            text="Calculus",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Pythagoras = Button(
            text="Pythagoras Theorem",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Circle_Perimeter = Button(
            text="Perimeter of Circle",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Circle_Area = Button(
            text="Area of Circle",
            font_size=16,
            size_hint_y=None,
            height=45
        )
        
        Rational_Numbers = Button(
            text="Rational Numbers",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Quadratic_Equations = Button(
            text="Quadratic Equations",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Congruence_of_Triangles = Button(
            text="Congruence of Triangles",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Laws_of_Exponents = Button(
            text="Laws of Exponents",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Algebraic_Identities = Button(
            text="Algebraic Identities",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Factorization_Algebraic_Expressions = Button(
            text="Factorization of Algebraic Expressions",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Polynomials = Button(
            text="Polynomials",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Arithmetic_Progressions = Button(
            text="Arithmetic Progressions",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Euclidean_Geometry = Button(
            text="Euclidean Geometry",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Similarity_of_Triangles = Button(
            text="Similarity of Triangles",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Areas_Parallelograms_Triangles = Button(
            text="Areas of Parallelograms and Triangles",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Circle_Chords_Arcs = Button(
            text="Circles: Chords and Arcs",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Surface_Area_Cubes_Cuboids = Button(
            text="Surface Area of Cubes and Cuboids",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Surface_Area_Cylinders_Cones = Button(
            text="Surface Area of Cylinders and Cones",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Volume_Cylinders_Cones_Spheres = Button(
            text="Volume of Cylinders, Cones and Spheres",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Herons_Formula = Button(
            text="Heron's Formula",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Trigonometric_Ratios = Button(
            text="Trigonometric Ratios",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Trigonometric_Identities = Button(
            text="Trigonometric Identities",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Heights_and_Distances = Button(
            text="Heights and Distances",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Statistics_Mean_Median_Mode = Button(
            text="Statistics: Mean, Median and Mode",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Grouped_Data_Frequency_Tables = Button(
            text="Grouped Data and Frequency Tables",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Probability_Compound_Events = Button(
            text="Probability of Compound Events",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Permutations_Combinations = Button(
            text="Permutations and Combinations",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Profit_Loss_Discount = Button(
            text="Profit, Loss and Discount",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Compound_Interest = Button(
            text="Compound Interest",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Tax_Financial_Mathematics = Button(
            text="Tax and Financial Mathematics",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Speed_Distance_Relative_Speed = Button(
            text="Speed, Distance and Relative Speed",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Time_and_Work = Button(
            text="Time and Work",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Pipes_and_Cisterns = Button(
            text="Pipes and Cisterns",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Ratio_Proportion_Word_Problems = Button(
            text="Ratio and Proportion Word Problems",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Mixtures_Alligation = Button(
            text="Mixtures and Alligation",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Unitary_Method = Button(
            text="Unitary Method in Real-Life Problems",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Percentage_Applications = Button(
            text="Percentage Applications",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        HCF_LCM_Word_Problems = Button(
            text="HCF and LCM Word Problems",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Decimal_Fraction_Word_Problems = Button(
            text="Decimal and Fraction Word Problems",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Rational_Algebraic_Expressions = Button(
            text="Rational Algebraic Expressions",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Linear_Inequalities = Button(
            text="Linear Inequalities",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Graphs_Linear_Equations = Button(
            text="Graphs of Linear Equations",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Systems_Linear_Equations = Button(
            text="Systems of Linear Equations",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Symmetry_Transformations = Button(
            text="Symmetry and Transformations",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Construction_Geometric_Figures = Button(
            text="Construction of Geometric Figures",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Angle_Properties_Theorems = Button(
            text="Angle Properties and Theorems",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Polygons_Interior_Angles = Button(
            text="Polygons and Interior Angles",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Mathematical_Reasoning = Button(
            text="Mathematical Reasoning",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Data_Interpretation = Button(
            text="Data Interpretation",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Number_Theory_Divisibility = Button(
            text="Number Theory and Divisibility",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Mathematical_Word_Problems = Button(
            text="Mathematical Word Problems",
            font_size=16,
            size_hint_y=None,
            height=45
        )

        Back = Button(
            text = "Go Back to home page",
            font_size = 16,
            size_hint_y = None,
            height = 45,
            color = "black"
        )

        Back2 = Button(
            text = "Go Back to Lessons page",
            font_size = 16,
            size_hint_y=None,
            height = 45,
            color = "black"
        )

        def r(instance):
            RE = Label(
                text="A square root is a number that, when multiplied by itself, gives the original number.\nFor example, the square root of 25 is 5 because 5 × 5 = 25.\nThe symbol for square root is √.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(RE)


        def p(instance):
            PE = Label(
                text="A polygon is a closed, two-dimensional shape made from straight line segments.\nPolygons are named by the number of sides they have.\nA triangle has 3 sides\nA quadrilateral has 4 sides\nA pentagon has 5 sides\nA hexagon has 6 sides\nA heptagon has 7 sides\nA octagon has 8 sides\nA nonagon has 9 sides\nA decagon has 10 sides.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(PE)


        def a(instance):
            AE = Label(
                text="Area is the amount of surface inside a flat, two-dimensional shape.\nIt is measured in square units, such as cm² or m².\nDifferent shapes have different formulas.\nFor example, the area of a rectangle is length × width.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(AE)


        def s(instance):
            SE = Label(
                text="Squaring a number means multiplying the number by itself.\nFor example, 5² means 5 × 5, which equals 25. The small 2 is called an exponent or power.\nSquaring is useful in areas, equations, and many other parts of mathematics.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(SE)


        def c(instance):
            CE = Label(
                text="Cubing a number means multiplying the number by itself three times.\nFor example, 3³ means 3 × 3 × 3, which equals 27.\nThe small 3 is the exponent.\nCubes are also used when finding the volume of three-dimensional objects.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(CE)

        def fr(instance):
            fra = Label(
                text="A fraction represents a part of a whole. It has a numerator on top and a denominator on the bottom. For example, 3/4 means 3 out of 4 equal parts.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(fra)

        def de(instance):
            dec = Label(
                text="A decimal is another way of representing numbers using a decimal point. For example, 0.5 is equal to 1/2, and 0.25 is equal to 1/4.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(dec)

        def pe(instance):
            per = Label(
                text="A percentage represents a number out of 100. The symbol % means percent. For example, 25% means 25 out of 100, which is equal to 1/4.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(per)

        def inte(instance):
            integer = Label(
                text="Integers are whole numbers that can be positive, negative, or zero. Examples include -5, -2, 0, 3, and 8. Integers do not contain fractions or decimals.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(integer)

        def fa(instance):
            fac = Label(
                text="A factor is a number that divides another number exactly without leaving a remainder. For example, 3 is a factor of 12 because 12 ÷ 3 = 4.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(fac)

        def mu(instance):
            mul = Label(
                text="A multiple is the result of multiplying a number by a whole number. For example, the multiples of 5 include 5, 10, 15, 20, and 25.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(mul)

        def pr(instance):
            prime = Label(
                text="A prime number is a whole number greater than 1 that has exactly two factors: 1 and itself. Examples include 2, 3, 5, 7, and 11.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(prime)

        def lcm(instance):
            text = Label(
                text="LCM means Least Common Multiple. It is the smallest positive number that is a multiple of two or more numbers. For example, the LCM of 4 and 6 is 12.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def hcf(instance):
            text = Label(
                text="HCF means Highest Common Factor. It is the largest number that divides two or more numbers exactly. For example, the HCF of 12 and 18 is 6.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def ratio_simplest(instance):
            text = Label(
                text=(
                    "RATIO: SIMPLEST FORM\n\n"
                    "A ratio compares two or more quantities.\n\n"
                    "To simplify a ratio, divide both parts by "
                    "their highest common factor (HCF).\n\n"
                    "Example:\n"
                    "12:18\n\n"
                    "HCF of 12 and 18 = 6\n\n"
                    "12 ÷ 6 : 18 ÷ 6\n"
                    "= 2:3\n\n"
                    "Therefore, the simplest form of 12:18 is 2:3."
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=400
            )

            show_lesson(text)


        def ratio_missing_part(instance):
            text = Label(
                text=(
                    "RATIO: FINDING A MISSING PART\n\n"
                    "Ratios can be used to find an unknown quantity.\n\n"
                    "Example:\n"
                    "The ratio of boys to girls is 2:3.\n"
                    "There are 8 boys. How many girls are there?\n\n"
                    "2 parts = 8 boys\n"
                    "1 part = 8 ÷ 2 = 4\n"
                    "3 parts = 3 × 4 = 12\n\n"
                    "Therefore, there are 12 girls.\n\n"
                    "Answer: 12"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=400
            )

            show_lesson(text)

        def pro(instance):
            text = Label(
                text="A proportion states that two ratios are equal. For example, 2:4 and 3:6 are proportional because both ratios represent the same relationship.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def av(instance):
            text = Label(
                text="The average, or mean, is found by adding all the numbers and dividing the total by the number of values. For example, the average of 4, 6, and 8 is 6.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def pl(instance):
            text = Label(
                text="Profit is the amount gained when the selling price is greater than the cost price. Loss occurs when the selling price is less than the cost price.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def si(instance):
            text = Label(
                text="Simple interest is the interest calculated only on the original principal amount. The formula is SI = (P × R × T) ÷ 100, where P is principal, R is rate, and T is time.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def sp(instance):
            text = Label(
                text="Speed tells us how fast something moves. Speed can be calculated using the formula Speed = Distance ÷ Time. For example, 100 km in 2 hours is 50 km/h.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def di(instance):
            text = Label(
                text="Distance tells us how far something travels. Distance can be calculated using Distance = Speed × Time. For example, at 60 km/h for 2 hours, the distance is 120 km.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def ti(instance):
            text = Label(
                text="Time tells us how long an event or journey takes. Using speed and distance, Time = Distance ÷ Speed. Time can be measured in seconds, minutes, hours, and other units.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def al(instance):
            text = Label(
                text="Algebra uses letters and symbols to represent unknown or changing numbers. For example, in x + 5 = 10, x represents the unknown number, which is 5.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def le(instance):
            text = Label(
                text="A linear equation is an equation in which the variable has a power of 1. For example, 2x + 3 = 9 is a linear equation. Solving it gives x = 3.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def ex(instance):
            text = Label(
                text="An exponent tells us how many times a number is multiplied by itself. For example, 2³ means 2 × 2 × 2 = 8. The 3 is the exponent.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def oo(instance):
            text = Label(
                text="The order of operations tells us the order in which calculations should be performed. Brackets come first, followed by exponents, multiplication and division, then addition and subtraction.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def pm(instance):
            text = Label(
                text="Perimeter is the total distance around the outside of a shape. For a rectangle, the formula is Perimeter = 2 × (length + width).",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def vo(instance):
            text = Label(
                text="Volume measures the amount of space inside a three-dimensional object. The volume of a rectangular box is length × width × height, measured in cubic units.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def tr(instance):
            text = Label(
                text="A triangle is a polygon with three sides and three angles. The interior angles of every triangle add up to 180 degrees.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def qu(instance):
            text = Label(
                text="A quadrilateral is a polygon with four sides and four angles. Examples include squares, rectangles, parallelograms, and trapezoids.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def ci(instance):
            text = Label(
                text="A circle is a round, two-dimensional shape in which every point on the edge is the same distance from the center. That distance is called the radius.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def an(instance):
            text = Label(
                text="An angle is formed when two lines or rays meet at a point. Angles are measured in degrees. Common types include acute, right, obtuse, and straight angles.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def co(instance):
            text = Label(
                text="Coordinates are used to locate points on a graph. A point is usually written as (x, y), where x shows the horizontal position and y shows the vertical position.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def prob(instance):
            text = Label(
                text="Probability describes how likely something is to happen. It ranges from 0 to 1, or from 0% to 100%. A probability of 0 means impossible and 1 means certain.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def stat(instance):
            text = Label(
                text="Statistics is the study of collecting, organizing, analyzing, and interpreting data. Averages, tables, graphs, and charts are commonly used in statistics.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def pat(instance):
            text = Label(
                text="A pattern is a sequence that follows a particular rule. For example, 2, 4, 6, 8 follows the rule of adding 2 each time.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)

        def seq(instance):
            text = Label(
                text="A sequence is an ordered list of numbers or objects that follows a rule. For example, 3, 6, 9, 12 is a sequence that increases by 3 each time.",
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=150
            )
            show_lesson(text)
        
        def cos(instance):
            text = Label(
                text=(
                    "COSINE (cos θ)\n\n"
                    "cos θ = Adjacent ÷ Hypotenuse\n\n"
                    "Exact values:\n\n"
                    "cos 0° = 1\n"
                    "cos 30° = √3/2\n"
                    "cos 45° = √2/2\n"
                    "cos 60° = 1/2\n"
                    "cos 90° = 0"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=350
            )

            show_lesson(text)
            
        def sin(instance):
            text = Label(
                text=(
                    "SINE (sin θ)\n\n"
                    "sin θ = Opposite ÷ Hypotenuse\n\n"
                    "Exact values:\n\n"
                    "sin 0° = 0\n"
                    "sin 30° = 1/2\n"
                    "sin 45° = √2/2\n"
                    "sin 60° = √3/2\n"
                    "sin 90° = 1"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=350
            )

            show_lesson(text)

        def tan(instance):
            text = Label(
                text=(
                    "TANGENT (tan θ)\n\n"
                    "tan θ = Opposite ÷ Adjacent\n\n"
                    "Exact values:\n\n"
                    "tan 0° = 0\n"
                    "tan 30° = √3/3\n"
                    "tan 45° = 1\n"
                    "tan 60° = √3\n"
                    "tan 90° = Undefined"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=350
            )
            show_lesson(text)


        def cosec(instance):
            text = Label(
                text=(
                    "COSECANT (cosec θ)\n\n"
                    "cosec θ = 1 ÷ sin θ\n"
                    "cosec θ = Hypotenuse ÷ Opposite\n\n"
                    "Exact values:\n\n"
                    "cosec 0° = Undefined\n"
                    "cosec 30° = 2\n"
                    "cosec 45° = √2\n"
                    "cosec 60° = 2√3/3\n"
                    "cosec 90° = 1"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=400
            )

            show_lesson(text)

        def sec(instance):
            text = Label(
                text=(
                    "SECANT (sec θ)\n\n"
                    "sec θ = 1 ÷ cos θ\n"
                    "sec θ = Hypotenuse ÷ Adjacent\n\n"
                    "Exact values:\n\n"
                    "sec 0° = 1\n"
                    "sec 30° = 2√3/3\n"
                    "sec 45° = √2\n"
                    "sec 60° = 2\n"
                    "sec 90° = Undefined"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=400
            )

            show_lesson(text)


        def cot(instance):
            text = Label(
                text=(
                    "COTANGENT (cot θ)\n\n"
                    "cot θ = 1 ÷ tan θ\n"
                    "cot θ = Adjacent ÷ Opposite\n\n"
                    "Exact values:\n\n"
                    "cot 0° = Undefined\n"
                    "cot 30° = √3\n"
                    "cot 45° = 1\n"
                    "cot 60° = √3/3\n"
                    "cot 90° = 0"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=400
            )

            show_lesson(text)

        def natural_sum(instance):
            text = Label(
                text=(
                    "SUM OF NATURAL NUMBERS\n\n"
                    "Natural numbers are 1, 2, 3, 4, ...\n\n"
                    "Formula:\n\n"
                    "[u]n(n+1)[/u]\n"
                    "────────\n"
                    "     2\n\n"
                    "Example: Find the sum of the first 5 natural numbers.\n\n"
                    "n = 5\n\n"
                    "5 × (5 + 1) ÷ 2\n"
                    "= 5 × 6 ÷ 2\n"
                    "= 30 ÷ 2\n"
                    "= 15\n\n"
                    "Answer: 15"
                ),
                markup=True,
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=450
            )

            show_lesson(text)
            
        def odd_sum(instance):
            text = Label(
                text=(
                    "SUM OF ODD NUMBERS\n\n"
                    "Formula:\n\n"
                    "1 + 3 + 5 + ... + (2n - 1) = n²\n\n"
                    "The symbol ² means squared.\n\n"
                    "Example: Find the sum of the first 5 odd numbers.\n\n"
                    "n = 5\n\n"
                    "n² = 5²\n"
                    "= 5 × 5\n"
                    "= 25\n\n"
                    "Check:\n"
                    "1 + 3 + 5 + 7 + 9 = 25\n\n"
                    "Answer: 25"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=450
            )

            show_lesson(text)

        def even_sum(instance):
            text = Label(
                text=(
                    "SUM OF EVEN NUMBERS\n\n"
                    "Formula:\n\n"
                    "2 + 4 + 6 + ... + 2n = n(n+1)\n\n"
                    "Example: Find the sum of the first 5 even numbers.\n\n"
                    "n = 5\n\n"
                    "n(n+1)\n"
                    "= 5 × (5 + 1)\n"
                    "= 5 × 6\n"
                    "= 30\n\n"
                    "Check:\n"
                    "2 + 4 + 6 + 8 + 10 = 30\n\n"
                    "Answer: 30"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=450
            )

            show_lesson(text)
            
        def square_identities(instance):
            text = Label(
                text=(
                    "ALGEBRAIC SQUARE IDENTITIES\n\n"
                    "1. Difference of two squares\n\n"
                    "a² − b² = (a+b)(a−b)\n\n"
                    "Example:\n"
                    "25² − 5²\n"
                    "= (25+5)(25−5)\n"
                    "= 30 × 20\n"
                    "= 600\n\n"
                    "2. Square of a sum\n\n"
                    "(a+b)² = a² + 2ab + b²\n\n"
                    "Example:\n"
                    "(x+3)² = x² + 6x + 9\n\n"
                    "3. Square of a difference\n\n"
                    "(a−b)² = a² − 2ab + b²\n\n"
                    "Example:\n"
                    "(x−3)² = x² − 6x + 9"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=650
            )

            show_lesson(text)
            
        def calculus(instance):
            text = Label(
                text=(
                    "CALCULUS\n\n"
                    "Calculus is a branch of mathematics that studies "
                    "change and accumulation.\n\n"
                    "It has two main parts:\n\n"
                    "1. Differentiation\n"
                    "It measures the rate of change.\n"
                    "It is related to the slope of a curve.\n\n"
                    "Example:\n"
                    "If y = x², then\n"
                    "dy/dx = 2x\n\n"
                    "2. Integration\n"
                    "It is used to find accumulation and area "
                    "under a curve.\n\n"
                    "Differentiation studies change.\n"
                    "Integration studies accumulation."
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=450
            )

            show_lesson(text)
            
        def pythagoras(instance):
            text = Label(
                text=(
                    "PYTHAGORAS THEOREM\n\n"
                    "In a right-angled triangle:\n\n"
                    "a² + b² = c²\n\n"
                    "c is the hypotenuse, which is the longest side "
                    "and is opposite the right angle.\n\n"
                    "Example:\n"
                    "a = 3\n"
                    "b = 4\n\n"
                    "c² = 3² + 4²\n"
                    "c² = 9 + 16\n"
                    "c² = 25\n"
                    "c = 5\n\n"
                    "Answer: The hypotenuse is 5."
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=400
            )

            show_lesson(text)
            
        def circle_perimeter(instance):
            text = Label(
                text=(
                    "PERIMETER OF A CIRCLE\n\n"
                    "The perimeter of a circle is called "
                    "its circumference.\n\n"
                    "Formula:\n"
                    "C = 2πr\n\n"
                    "or\n\n"
                    "C = πd\n\n"
                    "r = radius\n"
                    "d = diameter\n"
                    "π ≈ 3.14\n\n"
                    "Example:\n"
                    "Radius = 7 cm\n\n"
                    "C = 2 × π × 7\n"
                    "C ≈ 2 × 22/7 × 7\n"
                    "C ≈ 44 cm\n\n"
                    "Answer: 44 cm"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=450
            )

            show_lesson(text)
            
        def circle_area(instance):
            text = Label(
                text=(
                    "AREA OF A CIRCLE\n\n"
                    "The area is the space inside a circle.\n\n"
                    "Formula:\n"
                    "A = πr²\n\n"
                    "r = radius\n"
                    "π ≈ 3.14\n\n"
                    "Example:\n"
                    "Radius = 7 cm\n\n"
                    "A = π × 7²\n"
                    "A = 22/7 × 7 × 7\n"
                    "A = 154 cm²\n\n"
                    "Answer: 154 cm²"
                ),
                font_size=18,
                color=(0, 1, 0, 1),
                size_hint_y=None,
                height=400
            )

            show_lesson(text)
            
        def cube_root_trick(instance):
            text = Label(
                text = (
                    "CUBE ROOT TRICK\n\n"
                    "To find the cube root of a perfect cube:\n\n"
                    "Example: ∛12167\n\n"
                    "Step 1: Separate the number into groups of 3 digits from the right:\n"
                    "12 | 167\n\n"
                    "Step 2: Find the largest cube less than or equal to 12:\n"
                    "2³ = 8\n"
                    "3³ = 27 (too large)\n"
                    "First digit = 2\n\n"
                    "Step 3: Look at the last three digits: 167.\n"
                    "The cube ending in 167 is 23³.\n\n"
                    "Therefore:\n"
                    "∛12167 = 23\n\n"
                    "Remember common cubes:\n"
                    "1³ = 1    2³ = 8    3³ = 27\n"
                    "4³ = 64   5³ = 125  6³ = 216\n"
                    "7³ = 343  8³ = 512  9³ = 729\n"
                    "10³ = 1000"
                )
            )
            show_lesson(text)

        def Rational(self, instance):
            self.show_topic(
                "Rational Numbers",
                "Rational numbers can be written as p/q, where p and q are integers and q is not zero.\n\nExamples: 1/2, -3/4, 5"
            )


        def Quadratic(self, instance):
            self.show_topic(
                "Quadratic Equations",
                "A quadratic equation has the highest power of the variable as 2.\n\nStandard form: ax² + bx + c = 0"
            )


        def Congruence(self, instance):
            self.show_topic(
                "Congruence of Triangles",
                "Two triangles are congruent when they have the same shape and size.\n\nRules include SSS, SAS, ASA and RHS."
            )


        def Laws(self, instance):
            self.show_topic(
                "Laws of Exponents",
                "Important laws:\naᵐ × aⁿ = aᵐ⁺ⁿ\naᵐ ÷ aⁿ = aᵐ⁻ⁿ\n(aᵐ)ⁿ = aᵐⁿ"
            )


        def Identities(self, instance):
            self.show_topic(
                "Algebraic Identities",
                "(a + b)² = a² + 2ab + b²\n(a - b)² = a² - 2ab + b²\na² - b² = (a + b)(a - b)"
            )


        def Factorization(self, instance):
            self.show_topic(
                "Factorization of Algebraic Expressions",
                "Factorization means writing an expression as a product of its factors.\n\nExample: x² + 5x + 6 = (x + 2)(x + 3)"
            )


        def Polynomial(self, instance):
            self.show_topic(
                "Polynomials",
                "A polynomial is an expression containing variables and coefficients with non-negative whole-number powers.\n\nExample: 3x² + 2x + 5"
            )


        def Progression(self, instance):
            self.show_topic(
                "Arithmetic Progressions",
                "An arithmetic progression is a sequence where the difference between consecutive terms is constant.\n\nExample: 2, 5, 8, 11"
            )


        def Euclidean(self, instance):
            self.show_topic(
                "Euclidean Geometry",
                "Euclidean geometry studies points, lines, angles, shapes and geometric properties on a flat surface."
            )


        def Similarity(self, instance):
            self.show_topic(
                "Similarity of Triangles",
                "Similar triangles have the same shape but not necessarily the same size.\n\nTheir corresponding angles are equal and corresponding sides are proportional."
            )


        def Areas(self, instance):
            self.show_topic(
                "Areas of Parallelograms and Triangles",
                "Area of a parallelogram = base × height\n\nArea of a triangle = 1/2 × base × height"
            )


        def Chords(self, instance):
            self.show_topic(
                "Circle Chords and Arcs",
                "A chord is a line segment joining two points on a circle.\n\nAn arc is a part of the circumference of a circle."
            )


        def CubeArea(self, instance):
            self.show_topic(
                "Surface Area of Cubes and Cuboids",
                "Surface area of a cube = 6a²\n\nTotal surface area of a cuboid = 2(lw + lh + wh)"
            )


        def CylinderArea(self, instance):
            self.show_topic(
                "Surface Area of Cylinders and Cones",
                "Curved surface area of a cylinder = 2πrh\n\nThe surface area of a cone depends on its radius and slant height."
            )


        def SolidVolume(self, instance):
            self.show_topic(
                "Volume of Cylinders, Cones and Spheres",
                "Volume of a cylinder = πr²h\n\nVolume of a cone = 1/3πr²h\n\nVolume of a sphere = 4/3πr³"
            )


        def Heron(self, instance):
            self.show_topic(
                "Heron's Formula",
                "Heron's formula calculates the area of a triangle using its three sides.\n\nArea = √(s(s-a)(s-b)(s-c))"
            )


        def TrigRatios(self, instance):
            self.show_topic(
                "Trigonometric Ratios",
                "sin θ = Opposite / Hypotenuse\ncos θ = Adjacent / Hypotenuse\ntan θ = Opposite / Adjacent"
            )


        def TrigIdentities(self, instance):
            self.show_topic(
                "Trigonometric Identities",
                "Important identity:\n\nsin²θ + cos²θ = 1\n\ntan θ = sin θ / cos θ"
            )


        def Heights(self, instance):
            self.show_topic(
                "Heights and Distances",
                "Heights and distances use trigonometric ratios to calculate unknown lengths and angles in right-angled triangles."
            )


        def StatisticsMean(self, instance):
            self.show_topic(
                "Statistics: Mean, Median and Mode",
                "Mean = Sum of values / Number of values\n\nMedian is the middle value.\n\nMode is the most frequently occurring value."
            )


        def GroupedData(self, instance):
            self.show_topic(
                "Grouped Data and Frequency Tables",
                "Grouped data is organized into class intervals.\n\nA frequency table shows how often values or groups occur."
            )


        def CompoundProbability(self, instance):
            self.show_topic(
                "Probability of Compound Events",
                "Compound probability involves two or more events.\n\nFor independent events, multiply their probabilities when finding the probability that both occur."
            )


        def Permutations(self, instance):
            self.show_topic(
                "Permutations and Combinations",
                "Permutations involve arrangements where order matters.\n\nCombinations involve selections where order does not matter."
            )


        def Discount(self, instance):
            self.show_topic(
                "Profit, Loss and Discount",
                "Profit = Selling Price - Cost Price\n\nLoss = Cost Price - Selling Price\n\nDiscount = Marked Price - Selling Price"
            )


        def CompoundInterest(self, instance):
            self.show_topic(
                "Compound Interest",
                "Compound interest is calculated on the principal and accumulated interest.\n\nAmount = P(1 + R/100)ⁿ"
            )


        def Tax(self, instance):
            self.show_topic(
                "Tax and Financial Mathematics",
                "Tax is an amount added to the price of goods or services.\n\nTax = Tax rate × Original amount / 100"
            )


        def RelativeSpeed(self, instance):
            self.show_topic(
                "Speed, Distance and Relative Speed",
                "Speed = Distance / Time\n\nWhen two objects move in opposite directions, their relative speed is the sum of their speeds."
            )


        def Work(self, instance):
            self.show_topic(
                "Time and Work",
                "Work rate = 1 / Time taken\n\nWhen people work together, their work rates can be added."
            )


        def Pipes(self, instance):
            self.show_topic(
                "Pipes and Cisterns",
                "Pipes can fill or empty a tank.\n\nFilling pipes add work rate, while emptying pipes subtract work rate."
            )


        def RatioProblems(self, instance):
            self.show_topic(
                "Ratio and Proportion Word Problems",
                "A ratio compares quantities.\n\nA proportion states that two ratios are equal."
            )


        def Mixtures(self, instance):
            self.show_topic(
                "Mixtures and Alligation",
                "Mixtures combine two or more quantities.\n\nAlligation helps calculate the ratio in which different items should be mixed."
            )


        def Unitary(self, instance):
            self.show_topic(
                "Unitary Method",
                "The unitary method finds the value of one unit first and then uses it to calculate the required value."
            )


        def PercentApplications(self, instance):
            self.show_topic(
                "Percentage Applications",
                "Percentage = Part / Whole × 100\n\nPercentages are used in discounts, profit, loss, tax and marks."
            )


        def HCFProblems(self, instance):
            self.show_topic(
                "HCF and LCM Word Problems",
                "HCF is the greatest common factor.\n\nLCM is the least common multiple.\n\nBoth are useful for solving number-based word problems."
            )


        def DecimalProblems(self, instance):
            self.show_topic(
                "Decimal and Fraction Word Problems",
                "Fractions represent parts of a whole.\n\nDecimals are another way to represent fractions using a decimal point."
            )


        def RationalAlgebra(self, instance):
            self.show_topic(
                "Rational Algebraic Expressions",
                "A rational algebraic expression is a fraction containing algebraic expressions.\n\nExample: (x + 2) / (x + 3)"
            )


        def Inequalities(self, instance):
            self.show_topic(
                "Linear Inequalities",
                "A linear inequality compares expressions using symbols such as <, >, ≤ and ≥.\n\nExample: 2x + 3 > 7"
            )


        def LinearGraphs(self, instance):
            self.show_topic(
                "Graphs of Linear Equations",
                "A linear equation can be represented by a straight line on a coordinate graph.\n\nExample: y = 2x + 1"
            )


        def Systems(self, instance):
            self.show_topic(
                "Systems of Linear Equations",
                "A system of linear equations contains two or more equations with common variables.\n\nThe solution satisfies all equations."
            )


        def Symmetry(self, instance):
            self.show_topic(
                "Symmetry and Transformations",
                "Symmetry means that a shape has matching parts.\n\nTransformations include translation, rotation, reflection and enlargement."
            )


        def Construction(self, instance):
            self.show_topic(
                "Construction of Geometric Figures",
                "Geometric constructions use tools such as a ruler and compass to create accurate lines, angles and shapes."
            )


        def AngleProperties(self, instance):
            self.show_topic(
                "Angle Properties and Theorems",
                "Angles on a straight line add up to 180°.\n\nAngles around a point add up to 360°.\n\nVertically opposite angles are equal."
            )


        def PolygonAngles(self, instance):
            self.show_topic(
                "Polygons and Interior Angles",
                "The sum of the interior angles of a polygon with n sides is:\n\n(n - 2) × 180°"
            )


        def Reasoning(self, instance):
            self.show_topic(
                "Mathematical Reasoning",
                "Mathematical reasoning uses logical steps, statements and evidence to solve problems and reach conclusions."
            )


        def DataInterpretation(self, instance):
            self.show_topic(
                "Data Interpretation",
                "Data interpretation involves reading and analyzing tables, graphs, charts and diagrams to answer questions."
            )


        def Divisibility(self, instance):
            self.show_topic(
                "Number Theory and Divisibility",
                "Divisibility rules help determine whether a number can be divided exactly by another number."
            )


        def WordProblems(self, instance):
            self.show_topic(
                "Mathematical Word Problems",
                "Word problems describe real-life situations using mathematics.\n\nRead carefully, identify the known values and choose the correct operation or formula."
            )

        Root.bind(on_press=r)
        Square.bind(on_press=s)
        Cube.bind(on_press=c)
        Polygon.bind(on_press=p)
        Area.bind(on_press=a)
        Fractions.bind(on_press=fr)
        Decimals.bind(on_press=de)
        Percentages.bind(on_press=pe)
        Integers.bind(on_press=inte)
        Factors.bind(on_press=fa)
        Multiples.bind(on_press=mu)
        Prime_Numbers.bind(on_press=pr)
        LCM.bind(on_press=lcm)
        HCF.bind(on_press=hcf)
        Ratio_Missing.bind(on_press=ratio_missing_part)
        Ratio_Simplest.bind(on_press=ratio_simplest)
        Proportion.bind(on_press=pro)
        Average.bind(on_press=av)
        Profit_Loss.bind(on_press=pl)
        Simple_Interest.bind(on_press=si)
        Speed.bind(on_press=sp)
        Distance.bind(on_press=di)
        Time.bind(on_press=ti)
        Algebra.bind(on_press=al)
        Linear_Equations.bind(on_press=le)
        Exponents.bind(on_press=ex)
        Order_of_Operations.bind(on_press=oo)
        Perimeter.bind(on_press=pm)
        Volume.bind(on_press=vo)
        Triangles.bind(on_press=tr)
        Quadrilaterals.bind(on_press=qu)
        Circles.bind(on_press=ci)
        Natural_Sum.bind(on_press=natural_sum)
        Odd_Sum.bind(on_press=odd_sum)
        Even_Sum.bind(on_press=even_sum)
        Cube_Root_Trick.bind(on_press=cube_root_trick)
        Square_Identities.bind(on_press=square_identities)
        Calculus.bind(on_press=calculus)
        Pythagoras.bind(on_press=pythagoras)
        Circle_Perimeter.bind(on_press=circle_perimeter)
        Circle_Area.bind(on_press=circle_area)
        Angles.bind(on_press=an)
        Coordinates.bind(on_press=co)
        Probability.bind(on_press=prob)
        Statistics.bind(on_press=stat)
        Patterns.bind(on_press=pat)
        Sequences.bind(on_press=seq)
        Sin.bind(on_press=sin)
        Cos.bind(on_press=cos)
        Tan.bind(on_press=tan)
        Cosec.bind(on_press=cosec)
        Sec.bind(on_press=sec)
        Cot.bind(on_press=cot)
        Rational_Numbers.bind(on_press=Rational)
        Quadratic_Equations.bind(on_press=Quadratic)
        Congruence_of_Triangles.bind(on_press=Congruence)
        Laws_of_Exponents.bind(on_press=Laws)
        Algebraic_Identities.bind(on_press=Identities)
        Factorization_Algebraic_Expressions.bind(on_press=Factorization)
        Polynomials.bind(on_press=Polynomial)
        Arithmetic_Progressions.bind(on_press=Progression)
        Euclidean_Geometry.bind(on_press=Euclidean)
        Similarity_of_Triangles.bind(on_press=Similarity)
        Areas_Parallelograms_Triangles.bind(on_press=Areas)
        Circle_Chords_Arcs.bind(on_press=Chords)
        Surface_Area_Cubes_Cuboids.bind(on_press=CubeArea)
        Surface_Area_Cylinders_Cones.bind(on_press=CylinderArea)
        Volume_Cylinders_Cones_Spheres.bind(on_press=SolidVolume)
        Herons_Formula.bind(on_press=Heron)
        Trigonometric_Ratios.bind(on_press=TrigRatios)
        Trigonometric_Identities.bind(on_press=TrigIdentities)
        Heights_and_Distances.bind(on_press=Heights)
        Statistics_Mean_Median_Mode.bind(on_press=StatisticsMean)
        Grouped_Data_Frequency_Tables.bind(on_press=GroupedData)
        Probability_Compound_Events.bind(on_press=CompoundProbability)
        Permutations_Combinations.bind(on_press=Permutations)
        Profit_Loss_Discount.bind(on_press=Discount)
        Compound_Interest.bind(on_press=CompoundInterest)
        Tax_Financial_Mathematics.bind(on_press=Tax)
        Speed_Distance_Relative_Speed.bind(on_press=RelativeSpeed)
        Time_and_Work.bind(on_press=Work)
        Pipes_and_Cisterns.bind(on_press=Pipes)
        Ratio_Proportion_Word_Problems.bind(on_press=RatioProblems)
        Mixtures_Alligation.bind(on_press=Mixtures)
        Unitary_Method.bind(on_press=Unitary)
        Percentage_Applications.bind(on_press=PercentApplications)
        HCF_LCM_Word_Problems.bind(on_press=HCFProblems)
        Decimal_Fraction_Word_Problems.bind(on_press=DecimalProblems)
        Rational_Algebraic_Expressions.bind(on_press=RationalAlgebra)
        Linear_Inequalities.bind(on_press=Inequalities)
        Graphs_Linear_Equations.bind(on_press=LinearGraphs)
        Systems_Linear_Equations.bind(on_press=Systems)
        Symmetry_Transformations.bind(on_press=Symmetry)
        Construction_Geometric_Figures.bind(on_press=Construction)
        Angle_Properties_Theorems.bind(on_press=AngleProperties)
        Polygons_Interior_Angles.bind(on_press=PolygonAngles)
        Mathematical_Reasoning.bind(on_press=Reasoning)
        Data_Interpretation.bind(on_press=DataInterpretation)
        Number_Theory_Divisibility.bind(on_press=Divisibility)
        Mathematical_Word_Problems.bind(on_press=WordProblems)
        Back.bind(on_press=self.home)
        Back2.bind(on_press=self.Lesson)

        lesson_layout.add_widget(Back)
        lesson_layout.add_widget(Back2)
        lesson_layout.add_widget(Root)
        lesson_layout.add_widget(Square)
        lesson_layout.add_widget(Cube)
        lesson_layout.add_widget(Polygon)
        lesson_layout.add_widget(Area)
        lesson_layout.add_widget(Fractions)
        lesson_layout.add_widget(Decimals)
        lesson_layout.add_widget(Percentages)
        lesson_layout.add_widget(Integers)
        lesson_layout.add_widget(Factors)
        lesson_layout.add_widget(Multiples)
        lesson_layout.add_widget(Prime_Numbers)
        lesson_layout.add_widget(LCM)
        lesson_layout.add_widget(HCF)
        lesson_layout.add_widget(Ratio_Missing)
        lesson_layout.add_widget(Ratio_Simplest)
        lesson_layout.add_widget(Proportion)
        lesson_layout.add_widget(Average)
        lesson_layout.add_widget(Profit_Loss)
        lesson_layout.add_widget(Simple_Interest)
        lesson_layout.add_widget(Speed)
        lesson_layout.add_widget(Distance)
        lesson_layout.add_widget(Time)
        lesson_layout.add_widget(Algebra)
        lesson_layout.add_widget(Linear_Equations)
        lesson_layout.add_widget(Exponents)
        lesson_layout.add_widget(Order_of_Operations)
        lesson_layout.add_widget(Perimeter)
        lesson_layout.add_widget(Volume)
        lesson_layout.add_widget(Triangles)
        lesson_layout.add_widget(Quadrilaterals)
        lesson_layout.add_widget(Circles)
        lesson_layout.add_widget(Angles)
        lesson_layout.add_widget(Coordinates)
        lesson_layout.add_widget(Probability)
        lesson_layout.add_widget(Statistics)
        lesson_layout.add_widget(Patterns)
        lesson_layout.add_widget(Sequences)
        lesson_layout.add_widget(Cos)
        lesson_layout.add_widget(Sin)
        lesson_layout.add_widget(Tan)
        lesson_layout.add_widget(Cosec)
        lesson_layout.add_widget(Sec)
        lesson_layout.add_widget(Cot)
        lesson_layout.add_widget(Cube_Root_Trick)
        lesson_layout.add_widget(Square_Identities)
        lesson_layout.add_widget(Natural_Sum)
        lesson_layout.add_widget(Odd_Sum)
        lesson_layout.add_widget(Even_Sum)
        lesson_layout.add_widget(Calculus)
        lesson_layout.add_widget(Pythagoras)
        lesson_layout.add_widget(Circle_Perimeter)
        lesson_layout.add_widget(Circle_Area)
        lesson_layout.add_widget(Rational_Numbers)
        lesson_layout.add_widget(Quadratic_Equations)
        lesson_layout.add_widget(Congruence_of_Triangles)
        lesson_layout.add_widget(Laws_of_Exponents)
        lesson_layout.add_widget(Algebraic_Identities)
        lesson_layout.add_widget(Factorization_Algebraic_Expressions)
        lesson_layout.add_widget(Polynomials)
        lesson_layout.add_widget(Arithmetic_Progressions)
        lesson_layout.add_widget(Euclidean_Geometry)
        lesson_layout.add_widget(Similarity_of_Triangles)
        lesson_layout.add_widget(Areas_Parallelograms_Triangles)
        lesson_layout.add_widget(Circle_Chords_Arcs)
        lesson_layout.add_widget(Surface_Area_Cubes_Cuboids)
        lesson_layout.add_widget(Surface_Area_Cylinders_Cones)
        lesson_layout.add_widget(Volume_Cylinders_Cones_Spheres)
        lesson_layout.add_widget(Herons_Formula)
        lesson_layout.add_widget(Trigonometric_Ratios)
        lesson_layout.add_widget(Trigonometric_Identities)
        lesson_layout.add_widget(Heights_and_Distances)
        lesson_layout.add_widget(Statistics_Mean_Median_Mode)
        lesson_layout.add_widget(Grouped_Data_Frequency_Tables)
        lesson_layout.add_widget(Probability_Compound_Events)
        lesson_layout.add_widget(Permutations_Combinations)
        lesson_layout.add_widget(Profit_Loss_Discount)
        lesson_layout.add_widget(Compound_Interest)
        lesson_layout.add_widget(Tax_Financial_Mathematics)
        lesson_layout.add_widget(Speed_Distance_Relative_Speed)
        lesson_layout.add_widget(Time_and_Work)
        lesson_layout.add_widget(Pipes_and_Cisterns)
        lesson_layout.add_widget(Ratio_Proportion_Word_Problems)
        lesson_layout.add_widget(Mixtures_Alligation)
        lesson_layout.add_widget(Unitary_Method)
        lesson_layout.add_widget(Percentage_Applications)
        lesson_layout.add_widget(HCF_LCM_Word_Problems)
        lesson_layout.add_widget(Decimal_Fraction_Word_Problems)
        lesson_layout.add_widget(Rational_Algebraic_Expressions)
        lesson_layout.add_widget(Linear_Inequalities)
        lesson_layout.add_widget(Graphs_Linear_Equations)
        lesson_layout.add_widget(Systems_Linear_Equations)
        lesson_layout.add_widget(Symmetry_Transformations)
        lesson_layout.add_widget(Construction_Geometric_Figures)
        lesson_layout.add_widget(Angle_Properties_Theorems)
        lesson_layout.add_widget(Polygons_Interior_Angles)
        lesson_layout.add_widget(Mathematical_Reasoning)
        lesson_layout.add_widget(Data_Interpretation)
        lesson_layout.add_widget(Number_Theory_Divisibility)
        lesson_layout.add_widget(Mathematical_Word_Problems)

        scroll.add_widget(lesson_layout)
        self.page_layout.add_widget(scroll)

    def home(self, instance):
        self.stop_timer()
        self.home_page()

    def load_stats(self):
        try:
            with open("quiz_stats.json", "r") as file:
                data = json.load(file)

            self.passed_quizzes = data.get("passed", 0)
            self.failed_quizzes = data.get("failed", 0)

        except (FileNotFoundError, json.JSONDecodeError):
            self.passed_quizzes = 0
            self.failed_quizzes = 0


    def save_stats(self):
        data = {
            "passed": self.passed_quizzes,
            "failed": self.failed_quizzes
        }

        with open("quiz_stats.json", "w") as file:
            json.dump(data, file)
            
    def save_leaderboard(self):
        try:
            with open("leaderboard.json", "r") as file:
                leaderboard = json.load(file)

            if not isinstance(leaderboard, list):
                leaderboard = []

        except (FileNotFoundError, json.JSONDecodeError):
            leaderboard = []

        leaderboard.append({
            "name": str(self.student_name),
            "score": int(self.score),
            "class": int(self.selected_class)
        })

        def get_score(student):
            if not isinstance(student, dict):
                return 0

            try:
                return int(student.get("score", 0))
            except (TypeError, ValueError):
                return 0

        leaderboard.sort(
            key=get_score,
            reverse=True
        )

        with open("leaderboard.json", "w") as file:
            json.dump(leaderboard, file, indent=4)
    
    def new_question(self):
        if self.selected_class in [5, 6]:
            topics = [
                "Square", "Area", "Polygon", "Fractions",
                "Decimals", "Percentages", "Factors",
                "Multiples", "Prime Numbers", "LCM", "HCF",
                "Average", "Perimeter", "Triangles",
                "Angles", "Patterns", "Sequences",
                "Natural Numbers","Whole Numbers"
            ]

        elif self.selected_class in [7, 8]:
            topics = [
                "Root", "Square", "Cube", "Area", "Polygon",
                "Fractions", "Decimals", "Percentages", "Integers",
                "Factors", "Multiples", "Prime Numbers", "LCM", "HCF",
                "Ratio", "Proportion", "Average", "Algebra",
                "Exponents", "Order of Operations", "Perimeter",
                "Volume", "Triangles", "Quadrilaterals", "Angles",
                "Coordinates", "Probability", "Patterns", "Sequences",
                "Circles", "Circle Perimeter", "Circle Area","Rational Numbers",
                "Profit and Loss","Comparing Quantities",
                "Direct and Inverse Proportion","Squares and Square Roots",
                "Cubes and Cube Roots","Data Handling",
                "Symmetry"
            ]

        else:
            topics = [
                "Root", "Square", "Cube", "Area", "Polygon",
                "Fractions", "Decimals", "Percentages", "Integers",
                "Factors", "Multiples", "Prime Numbers", "LCM", "HCF",
                "Ratio", "Proportion", "Average", "Profit & Loss",
                "Simple Interest", "Speed", "Distance", "Time",
                "Algebra", "Linear Equations", "Exponents",
                "Order of Operations", "Perimeter", "Volume",
                "Triangles", "Quadrilaterals", "Circles",
                "Circle Perimeter", "Circle Area", "Angles",
                "Coordinates", "Probability", "Statistics",
                "Patterns", "Sequences", "Sine", "Cosine",
                "Tangent", "Cosecant", "Secant", "Cotangent",
                "Calculus","Algebraic Equations","Cube Root Trick",
                "Sum of Odd Numbers","Sum of Even Numbers",
                "Sum of Natural Numbers","Pythagoras","Number Systems",
                "Rational Numbers","Irrational Numbers",
                "Real Numbers","Polynomials",
                "Linear Equations in Two Variables",
                "Quadratic Equations","Arithmetic Progressions",
                "Euclidean Geometry","Congruence of Triangles",
                "Similarity of Triangles","Areas of Parallelograms and Triangles",
                "Surface Areas and Volumes","Heron's Formula",
                "Pythagoras Theorem","Trigonometric Ratios",
                "Trigonometric Identities","Heights and Distances","Mean, Median and Mode",
                "Financial Mathematics","Compound Interest",
                "Tax and Percentage Applications","Linear Inequalities",
                "Factorization","Algebraic Identities",
                "Systems of Linear Equations","Permutations and Combinations",
                "Mathematical Reasoning","Data Interpretation",
                "Number Theory"
            ]

        topic = random.choice(topics)
        self.quiz_topic = topic

        if topic == "Root":
            n = random.randint(1, 15)
            n = n * n
            self.correct_answer = int(n ** 0.5)
            self.question.text = f"√{n} = ?"

        elif topic == "Square":
            n = random.randint(2, 15)
            self.correct_answer = n * n
            self.question.text = f"What is {n}²?"

        elif topic == "Cube":
            n = random.randint(2, 10)
            self.correct_answer = n * n * n
            self.question.text = f"What is {n}³?"

        elif topic == "Area":
            length = random.randint(2, 15)
            width = random.randint(2, 15)
            self.correct_answer = length * width
            self.question.text = f"Area of a rectangle with length {length} and width {width}?"

        elif topic == "Polygon":
            sides = random.randint(3, 10)
            names = {
                3: "triangle",
                4: "quadrilateral",
                5: "pentagon",
                6: "hexagon",
                7: "heptagon",
                8: "octagon",
                9: "nonagon",
                10: "decagon"
            }
            self.correct_answer = sides
            self.question.text = f"How many sides does a {names[sides]} have?"

        elif topic == "Fractions":
            denominator = random.choice([2, 3, 4, 5, 6, 8, 10])
            numerator = random.randint(1, denominator - 1)
            self.correct_answer = numerator / denominator
            self.question.text = f"{numerator}/{denominator} = decimal?"

        elif topic == "Decimals":
            self.correct_answer = random.choice([0.25, 0.5, 0.75, 0.2, 0.4, 0.6, 0.8])
            self.question.text = f"Convert {self.correct_answer} to a percentage."

            self.correct_answer = int(self.correct_answer * 100)
            self.question.text = self.question.text

        elif topic == "Percentages":
            percentage = random.choice([10, 20, 25, 50, 75])
            number = random.choice([20, 40, 60, 80, 100])
            self.correct_answer = percentage * number / 100
            self.question.text = f"What is {percentage}% of {number}?"

        elif topic == "Integers":
            a = random.randint(-20, 20)
            b = random.randint(-20, 20)
            self.correct_answer = a + b
            self.question.text = f"{a} + ({b}) = ?"

        elif topic == "Factors":
            n = random.randint(2, 12)
            self.correct_answer = n
            self.question.text = f"Is {n} a factor of {n * random.randint(2, 8)}? Enter the factor."

        elif topic == "Multiples":
            n = random.randint(2, 12)
            multiple = random.randint(2, 10)
            self.correct_answer = n * multiple
            self.question.text = f"What is the {multiple}th multiple of {n}?"

        elif topic == "Prime Numbers":
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

            self.correct_answer = primes

            self.question.text = (
                "Give any prime number between 1 and 30:"
            )

        elif topic == "LCM":
            a = random.randint(2, 12)
            b = random.randint(2, 12)

            x = a
            while x % b != 0:
                x += a

            self.correct_answer = x
            self.question.text = f"LCM of {a} and {b} = ?"

        elif topic == "HCF":
            a = random.randint(4, 30)
            b = random.randint(4, 30)

            factors_a = [x for x in range(1, a + 1) if a % x == 0]
            factors_b = [x for x in range(1, b + 1) if b % x == 0]

            common = set(factors_a) & set(factors_b)

            self.correct_answer = max(common)
            self.question.text = f"HCF of {a} and {b} = ?"

        elif topic == "Ratio":
            ratio_type = random.choice([1, 2])

            if ratio_type == 1:
                a = random.randint(1, 12)
                b = random.randint(1, 12)

                common_factor = math.gcd(a, b)

                c = a * common_factor
                d = b * common_factor
                a //= common_factor
                b //= common_factor

                self.correct_answer = f"{a}:{b}"
                self.question.text = (
                    f"Simplify the ratio {c}:{d} "
                    f"to its simplest form."
                )

            else:
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                multiplier = random.randint(2, 6)

                first_part = a * multiplier
                second_part = b * multiplier

                self.correct_answer = second_part

                self.question.text = (
                    f"The ratio is {a}:{b}.\n"
                    f"If the first part is {first_part}, "
                    f"what is the second part?"
                )

        elif topic == "Proportion":
            a = random.randint(1, 5)
            b = random.randint(2, 8)
            c = random.randint(1, 5)

            self.correct_answer = (b * c) / a
            self.question.text = f"{a}:{b} = {c}: ?"

        elif topic == "Average":
            numbers = [random.randint(1, 20) for _ in range(3)]
            self.correct_answer = sum(numbers) / 3
            self.question.text = f"Average of {numbers[0]}, {numbers[1]}, {numbers[2]} = ?"

        elif topic == "Profit & Loss":
            cost = random.randint(10, 50)
            selling = cost + random.randint(1, 20)

            self.correct_answer = selling - cost
            self.question.text = f"Cost = {cost}, Selling Price = {selling}. Profit = ?"

        elif topic == "Simple Interest":
            p = random.choice([100, 200, 500, 1000])
            r = random.choice([5, 10])
            t = random.choice([1, 2, 3])

            self.correct_answer = (p * r * t) / 100
            self.question.text = f"Find SI: P={p}, R={r}%, T={t} years."

        elif topic == "Speed":
            distance = random.choice([60, 100, 120, 150])
            time = random.choice([2, 3, 5])

            while distance % time != 0:
                distance = random.choice([60, 100, 120, 150])

            self.correct_answer = distance / time
            self.question.text = f"Distance = {distance} km, Time = {time} hours. Speed = ?"

        elif topic == "Distance":
            speed = random.choice([20, 30, 40, 50, 60])
            time = random.choice([2, 3, 4])

            self.correct_answer = speed * time
            self.question.text = f"Speed = {speed} km/h, Time = {time} h. Distance = ?"

        elif topic == "Time":
            speed = random.choice([20, 30, 40, 50])
            time = random.choice([2, 3, 4])
            distance = speed * time

            self.correct_answer = time
            self.question.text = f"Distance = {distance} km, Speed = {speed} km/h. Time = ?"

        elif topic == "Algebra":
            x = random.randint(1, 15)
            number = random.randint(1, 10)

            self.correct_answer = x
            self.question.text = f"x + {number} = {x + number}. Find x."

        elif topic == "Linear Equations":
            x = random.randint(1, 15)
            multiplier = random.randint(2, 5)
            number = random.randint(1, 10)

            self.correct_answer = x
            self.question.text = f"{multiplier}x + {number} = {multiplier * x + number}. Find x."

        elif topic == "Exponents":
            base = random.randint(2, 5)
            exponent = random.randint(2, 3)

            self.correct_answer = base ** exponent
            self.question.text = f"{base}^{exponent} = ?"

        elif topic == "Order of Operations":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 5)

            self.correct_answer = a + b * c
            self.question.text = f"{a} + {b} × {c} = ?"

        elif topic == "Perimeter":
            length = random.randint(2, 15)
            width = random.randint(2, 15)

            self.correct_answer = 2 * (length + width)
            self.question.text = f"Rectangle: length={length}, width={width}. Perimeter = ?"

        elif topic == "Volume":
            length = random.randint(2, 8)
            width = random.randint(2, 8)
            height = random.randint(2, 8)

            self.correct_answer = length * width * height
            self.question.text = f"Volume: {length} × {width} × {height} = ?"

        elif topic == "Triangles":
            self.correct_answer = 180
            self.question.text = "What is the total of the interior angles of a triangle?"

        elif topic == "Quadrilaterals":
            self.correct_answer = 360
            self.question.text = "What is the total of the interior angles of a quadrilateral?"

        elif topic == "Circles":
            radius = random.randint(2, 10)

            self.correct_answer = radius * 2
            self.question.text = f"A circle has radius {radius}. What is its diameter?"
            
        elif topic == "Circle Perimeter":
            radius = random.choice([7, 14, 21])
            self.correct_answer = round(2 * (22 / 7) * radius, 2)

            self.question.text = (
                f"Find the circumference of a circle "
                f"with radius {radius} cm. Use π = 22/7."
            )

        elif topic == "Circle Area":
            radius = random.choice([7, 14, 21])
            self.correct_answer = round((22 / 7) * radius * radius, 2)

            self.question.text = (
                f"Find the area of a circle "
                f"with radius {radius} cm. Use π = 22/7."
            )

        elif topic == "Angles":
            self.correct_answer = random.choice([90, 180, 360])
            self.question.text = f"How many degrees are in a {('right' if self.correct_answer == 90 else 'straight' if self.correct_answer == 180 else 'full')} angle?"

        elif topic == "Coordinates":
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)

            self.correct_answer = y
            self.question.text = f"What is the y-coordinate of ({x}, {y})?"

        elif topic == "Probability":
            total = random.choice([4, 5, 10])
            favourable = random.randint(1, total - 1)

            self.correct_answer = favourable / total
            self.question.text = f"Probability of an event with {favourable} favourable outcomes out of {total}? Enter as decimal."

        elif topic == "Statistics":
            numbers = [2, 4, 6, 8, 10]
            self.correct_answer = 6
            self.question.text = f"What is the mean of {numbers}?"

        elif topic == "Patterns":
            start = random.randint(1, 10)
            difference = random.randint(2, 5)

            numbers = [
                start,
                start + difference,
                start + difference * 2,
                start + difference * 3
            ]

            self.correct_answer = start + difference * 4
            self.question.text = f"{numbers[0]}, {numbers[1]}, {numbers[2]}, {numbers[3]}, ?"

        elif topic == "Sequences":
            start = random.randint(1, 10)
            difference = random.randint(2, 5)

            self.correct_answer = start + difference * 4
            self.question.text = (
                f"Sequence: {start}, "
                f"{start + difference}, "
                f"{start + difference * 2}, "
                f"{start + difference * 3}, ?"
            )
            
        elif topic == "Sine":
            opposite = random.randint(2, 9)
            hypotenuse = random.randint(opposite + 1, 15)

            self.correct_answer = round(opposite / hypotenuse, 2)
            self.question.text = (
                f"sin θ = Opposite / Hypotenuse\n"
                f"Opposite = {opposite}, Hypotenuse = {hypotenuse}\n"
                f"Find sin θ to 2 decimal places."
            )

        elif topic == "Cosine":
            adjacent = random.randint(2, 9)
            hypotenuse = random.randint(adjacent + 1, 15)

            self.correct_answer = round(adjacent / hypotenuse, 2)
            self.question.text = (
                f"cos θ = Adjacent / Hypotenuse\n"
                f"Adjacent = {adjacent}, Hypotenuse = {hypotenuse}\n"
                f"Find cos θ to 2 decimal places."
            )

        elif topic == "Tangent":
            opposite = random.randint(2, 9)
            adjacent = random.randint(2, 9)

            self.correct_answer = round(opposite / adjacent, 2)
            self.question.text = (
                f"tan θ = Opposite / Adjacent\n"
                f"Opposite = {opposite}, Adjacent = {adjacent}\n"
                f"Find tan θ to 2 decimal places."
            )

        elif topic == "Cosecant":
            opposite = random.randint(2, 9)
            hypotenuse = random.randint(opposite + 1, 15)

            self.correct_answer = round(hypotenuse / opposite, 2)
            self.question.text = (
                f"cosec θ = Hypotenuse / Opposite\n"
                f"Opposite = {opposite}, Hypotenuse = {hypotenuse}\n"
                f"Find cosec θ to 2 decimal places."
            )

        elif topic == "Secant":
            adjacent = random.randint(2, 9)
            hypotenuse = random.randint(adjacent + 1, 15)

            self.correct_answer = round(hypotenuse / adjacent, 2)
            self.question.text = (
                f"sec θ = Hypotenuse / Adjacent\n"
                f"Adjacent = {adjacent}, Hypotenuse = {hypotenuse}\n"
                f"Find sec θ to 2 decimal places."
            )

        elif topic == "Cotangent":
            opposite = random.randint(2, 9)
            adjacent = random.randint(2, 9)

            self.correct_answer = round(adjacent / opposite, 2)
            self.question.text = (
                f"cot θ = Adjacent / Opposite\n"
                f"Opposite = {opposite}, Adjacent = {adjacent}\n"
                f"Find cot θ to 2 decimal places."
            )
            
        elif topic == "Pythagoras":
            a = random.randint(3, 12)
            b = random.randint(3, 12)

            c = math.sqrt(a ** 2 + b ** 2)

            if c.is_integer():
                self.correct_answer = int(c)
                self.question.text = (
                    f"A right triangle has sides {a} cm and {b} cm. "
                    f"Find the hypotenuse using Pythagoras theorem."
                )
            else:
                self.correct_answer = round(c, 2)
                self.question.text = (
                    f"A right triangle has sides {a} cm and {b} cm. "
                    f"Find the hypotenuse. Round your answer to 2 decimal places."
                )


        elif topic == "Algebraic Equations":
            x = random.randint(1, 20)
            a = random.randint(2, 8)
            b = random.randint(1, 15)
            result = a * x + b

            self.correct_answer = x
            self.question.text = (
                f"Solve for x:\n"
                f"{a}x + {b} = {result}"
            )


        elif topic == "Cube Root Trick":
            cube_roots = [2, 3, 4, 5, 6, 7, 8, 9, 10]
            root = random.choice(cube_roots)
            number = root ** 3

            self.correct_answer = root
            self.question.text = (
                f"Find the cube root of {number}.\n"
                f"Use the cube root trick."
            )


        elif topic == "Sum of Odd Numbers":
            n = random.randint(2, 20)

            self.correct_answer = n ** 2
            self.question.text = (
                f"Find the sum of the first {n} odd numbers.\n"
                f"Use the formula: n²"
            )


        elif topic == "Sum of Even Numbers":
            n = random.randint(2, 20)

            self.correct_answer = n * (n + 1)
            self.question.text = (
                f"Find the sum of the first {n} even numbers.\n"
                f"Use the formula: n(n + 1)"
            )


        elif topic == "Sum of Natural Numbers":
            n = random.randint(2, 30)

            self.correct_answer = n * (n + 1) // 2
            self.question.text = (
                f"Find the sum of the first {n} natural numbers.\n"
                f"Use the formula: n(n + 1) / 2"
            )


        elif topic == "Calculus":
            x = random.randint(1, 10)

            self.correct_answer = 2 * x
            self.question.text = (
                f"Find the derivative of x² at x = {x}.\n"
                f"Use: d(x²)/dx = 2x"
            )
            
        elif topic == "Rational Numbers":
            a = random.randint(1, 9)
            b = random.randint(2, 10)
            self.correct_answer = round(a / b, 2)
            self.question.text = f"Convert {a}/{b} into a decimal. Round to 2 places."

        elif topic == "Quadratic Equations":
            x = random.randint(1, 10)
            b = random.randint(1, 10)
            c = x * x + b * x
            self.correct_answer = x
            self.question.text = f"Solve: x² + {b}x = {c}. Enter the positive x."

        elif topic == "Congruence of Triangles":
            self.correct_answer = 3
            self.question.text = "How many sides must be equal in the SSS congruence rule?"

        elif topic == "Laws of Exponents":
            base = random.randint(2, 5)
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            self.correct_answer = base ** (a + b)
            self.question.text = f"{base}^{a} × {base}^{b} = ?"

        elif topic == "Algebraic Identities":
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            self.correct_answer = (a + b) ** 2
            self.question.text = f"Find ({a} + {b})²."

        elif topic == "Factorization of Algebraic Expressions":
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            self.correct_answer = a + b
            self.question.text = f"If x² + {a + b}x + {a * b} = (x + a)(x + b), find a + b."

        elif topic == "Polynomials":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            x = random.randint(1, 5)
            self.correct_answer = a * x * x + b
            self.question.text = f"Find {a}x² + {b} when x = {x}."

        elif topic == "Arithmetic Progressions":
            first = random.randint(1, 10)
            difference = random.randint(1, 5)
            n = random.randint(3, 8)
            self.correct_answer = first + (n - 1) * difference
            self.question.text = f"Find term {n}: {first}, {first + difference}, {first + 2 * difference}, ..."

        elif topic == "Euclidean Geometry":
            self.correct_answer = 180
            self.question.text = "What is the sum of angles on a straight line?"

        elif topic == "Similarity of Triangles":
            a = random.randint(2, 8)
            multiplier = random.randint(2, 4)
            self.correct_answer = a * multiplier
            self.question.text = f"Similar triangles have a corresponding side of {a} cm. Scale factor = {multiplier}. Find the matching side."

        elif topic == "Areas of Parallelograms and Triangles":
            base = random.randint(2, 12)
            height = random.randint(2, 12)
            self.correct_answer = base * height
            self.question.text = f"Find the area of a parallelogram with base {base} and height {height}."

        elif topic == "Circles: Chords and Arcs":
            self.correct_answer = 2
            self.question.text = "A diameter is how many times the radius?"

        elif topic == "Surface Area of Cubes and Cuboids":
            side = random.randint(2, 8)
            self.correct_answer = 6 * side * side
            self.question.text = f"Find the total surface area of a cube with side {side} cm."

        elif topic == "Surface Area of Cylinders and Cones":
            radius = random.randint(2, 6)
            height = random.randint(2, 10)
            self.correct_answer = round(2 * math.pi * radius * height, 2)
            self.question.text = f"Find the curved surface area of a cylinder: r={radius}, h={height}. Use π = 3.14."

        elif topic == "Volume of Cylinders, Cones and Spheres":
            radius = random.randint(2, 6)
            height = random.randint(2, 10)
            self.correct_answer = round(3.14 * radius * radius * height, 2)
            self.question.text = f"Find the volume of a cylinder: r={radius}, h={height}. Use π = 3.14."

        elif topic == "Heron's Formula":
            a = 3
            b = 4
            c = 5
            self.correct_answer = 6
            self.question.text = f"Find the area of a triangle with sides {a}, {b} and {c} cm."

        elif topic == "Trigonometric Ratios":
            self.correct_answer = 0.5
            self.question.text = "If opposite = 3 and hypotenuse = 6, find sin θ."

        elif topic == "Trigonometric Identities":
            self.correct_answer = 1
            self.question.text = "What is sin²θ + cos²θ?"

        elif topic == "Heights and Distances":
            self.correct_answer = 5
            self.question.text = "A right triangle has opposite = 3 and adjacent = 4. Find the height if the scale factor is 1.25."

        elif topic == "Statistics: Mean, Median and Mode":
            numbers = [2, 4, 6, 8, 10]
            self.correct_answer = 6
            self.question.text = f"Find the mean of {numbers}."

        elif topic == "Grouped Data and Frequency Tables":
            frequency = [2, 3, 5]
            self.correct_answer = sum(frequency)
            self.question.text = f"Find the total frequency: {frequency}."

        elif topic == "Probability of Compound Events":
            self.correct_answer = 0.25
            self.question.text = "Two independent events each have probability 0.5. Find the probability that both happen."

        elif topic == "Permutations and Combinations":
            n = random.randint(3, 6)
            self.correct_answer = n * (n - 1)
            self.question.text = f"How many ways can 2 objects be arranged from {n} objects?"

        elif topic == "Profit, Loss and Discount":
            cost = random.choice([100, 200, 300, 500])
            profit = random.choice([10, 20, 30])
            self.correct_answer = cost + (cost * profit / 100)
            self.question.text = f"Cost price = {cost}. Profit = {profit}%. Find the selling price."

        elif topic == "Compound Interest":
            principal = random.choice([100, 200, 500])
            rate = 10
            years = 2
            self.correct_answer = principal * (1 + rate / 100) ** years
            self.question.text = f"Find the amount: P={principal}, R=10%, T=2 years."

        elif topic == "Tax and Financial Mathematics":
            price = random.choice([100, 200, 500])
            tax = 10
            self.correct_answer = price + (price * tax / 100)
            self.question.text = f"Price = {price}. Tax = 10%. Find the final price."

        elif topic == "Speed, Distance and Relative Speed":
            speed1 = random.choice([20, 30, 40])
            speed2 = random.choice([10, 20, 30])
            self.correct_answer = speed1 + speed2
            self.question.text = f"Two objects move in opposite directions at {speed1} km/h and {speed2} km/h. Find relative speed."

        elif topic == "Time and Work":
            days = random.choice([2, 4, 5, 10])
            self.correct_answer = 1 / days
            self.question.text = f"A person finishes a job in {days} days. What is their one-day work rate? Round to 2 places."

        elif topic == "Pipes and Cisterns":
            fill_time = random.choice([2, 4, 5, 10])
            self.correct_answer = 1 / fill_time
            self.question.text = f"A pipe fills a tank in {fill_time} hours. What part of the tank does it fill in one hour?"

        elif topic == "Ratio and Proportion Word Problems":
            a = random.randint(2, 8)
            b = random.randint(2, 8)
            multiplier = random.randint(2, 5)
            self.correct_answer = b * multiplier
            self.question.text = f"The ratio is {a}:{b}. If the first quantity is {a * multiplier}, find the second quantity."

        elif topic == "Mixtures and Alligation":
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            self.correct_answer = a + b
            self.question.text = f"A mixture contains {a} litres of water and {b} litres of juice. Find the total litres."

        elif topic == "Unitary Method in Real-Life Problems":
            price = random.choice([20, 30, 40, 50])
            quantity = random.randint(2, 5)
            self.correct_answer = price * quantity
            self.question.text = f"One item costs {price}. Find the cost of {quantity} items."

        elif topic == "Percentage Applications":
            percentage = random.choice([10, 20, 25, 50])
            amount = random.choice([100, 200, 400, 800])
            self.correct_answer = amount * percentage / 100
            self.question.text = f"Find {percentage}% of {amount}."

        elif topic == "HCF and LCM Word Problems":
            a = random.choice([4, 6, 8, 10, 12])
            b = random.choice([3, 5, 6, 9])
            self.correct_answer = math.gcd(a, b)
            self.question.text = f"Find the HCF of {a} and {b}."

        elif topic == "Decimal and Fraction Word Problems":
            numerator = random.randint(1, 8)
            denominator = random.choice([2, 4, 5, 10])
            self.correct_answer = numerator / denominator
            self.question.text = f"Convert {numerator}/{denominator} to a decimal."

        elif topic == "Rational Algebraic Expressions":
            numerator = random.randint(1, 10)
            denominator = random.randint(2, 10)
            self.correct_answer = round(numerator / denominator, 2)
            self.question.text = f"Evaluate the expression {numerator}/{denominator}. Round to 2 places."

        elif topic == "Linear Inequalities":
            x = random.randint(1, 10)
            number = random.randint(1, 10)
            result = x + number
            self.correct_answer = x
            self.question.text = f"If x + {number} = {result}, find x."

        elif topic == "Graphs of Linear Equations":
            x = random.randint(1, 10)
            multiplier = random.randint(2, 5)
            self.correct_answer = multiplier * x
            self.question.text = f"For y = {multiplier}x, find y when x = {x}."

        elif topic == "Systems of Linear Equations":
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            self.correct_answer = x + y
            self.question.text = f"If x={x} and y={y}, find x + y."

        elif topic == "Symmetry and Transformations":
            self.correct_answer = 4
            self.question.text = "How many lines of symmetry does a square have?"

        elif topic == "Construction of Geometric Figures":
            self.correct_answer = 90
            self.question.text = "How many degrees are in a right angle?"

        elif topic == "Angle Properties and Theorems":
            angle = random.randint(20, 80)
            self.correct_answer = 180 - angle
            self.question.text = f"Two angles on a straight line are {angle}° and ?. Find the missing angle."

        elif topic == "Polygons and Interior Angles":
            sides = random.randint(3, 8)
            self.correct_answer = (sides - 2) * 180
            self.question.text = f"Find the sum of interior angles of a polygon with {sides} sides."

        elif topic == "Mathematical Reasoning":
            self.correct_answer = 1
            self.question.text = "A statement that is either true or false is called a proposition. Enter 1 for true."

        elif topic == "Data Interpretation":
            values = [10, 20, 30, 40]
            self.correct_answer = sum(values)
            self.question.text = f"Find the total of this data: {values}."

        elif topic == "Number Theory and Divisibility":
            number = random.choice([12, 18, 24, 36, 48])
            self.correct_answer = 3
            self.question.text = f"How many positive factors does {number} have? Enter 3 if it has six factors."

        elif topic == "Mathematical Word Problems":
            price = random.randint(10, 50)
            quantity = random.randint(2, 5)
            self.correct_answer = price * quantity
            self.question.text = f"One notebook costs {price}. What is the cost of {quantity} notebooks?"

        self.answer.text = ""
        self.feedback.text = ""
        self.next_question.disabled = True
        
        Clock.schedule_once(lambda dt: setattr(self.answer, "focus", True), 0.1)

    def check_answer(self, instance):
        try:
            user_text = self.answer.text.strip()
            correct_text = str(self.correct_answer)

            if self.quiz_topic == "Ratio" and ":" in correct_text:
                user_ratio = user_text.replace(" ", "")
                correct_ratio = correct_text.replace(" ", "")

                user_parts = user_ratio.split(":")
                correct_parts = correct_ratio.split(":")

                if len(user_parts) == 2:
                    user_a = int(user_parts[0])
                    user_b = int(user_parts[1])

                    correct_a = int(correct_parts[0])
                    correct_b = int(correct_parts[1])

                    if user_b == 0 or correct_b == 0:
                        self.feedback.text = "Please enter a valid ratio."
                        return
                    
                    elif user_a * correct_b == correct_a * user_b:
                        self.score += 1
                        self.feedback.text = f"Correct answer!\nTopic : {self.quiz_topic}"
                    
                    else:
                        self.feedback.text = f"Wrong answer!\nCorrect answer: {self.correct_answer}"
                
                else:
                    self.feedback.text = (
                        f"Wrong answer!\nCorrect Answer: {self.correct_answer}"
                    )

            elif self.quiz_topic == "Prime Numbers":
                user_answer = int(user_text)

                if user_answer in self.correct_answer:
                    self.score += 1
                    self.feedback.text = f"Correct! ({self.quiz_topic})"
                else:
                    self.feedback.text = "Wrong! Enter a prime number between 1 and 30."

                self.submit.disabled = True
                self.next_question.disabled = False

                if self.question_number == 20:
                    self.next_question.text = "View Score"

            else:
                user_answer = float(user_text)
                correct_answer = float(self.correct_answer)

                if abs(user_answer - correct_answer) < 0.1:
                    self.score += 1
                    self.feedback.text = f"Correct! ({self.quiz_topic})"
                else:
                    self.feedback.text = (
                        f"Wrong! Answer: {self.correct_answer}"
                    )

            self.submit.disabled = True
            self.next_question.disabled = False

            if self.question_number == 20:
                self.next_question.text = "View Score"

        except (ValueError, ZeroDivisionError):
            self.feedback.text = "Please enter a valid answer."

    def next_question_pressed(self, instance):
        if self.question_number == 20:
            self.show_result()
        else:
            self.question_number += 1
            self.new_question()
            self.submit.disabled = False
            self.next_question.disabled = True

    def Maths_Quiz(self, instance):
        self.page_layout.clear_widgets()

        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=30
        )

        self.name_input = TextInput(
            hint_text="Enter your name",
            multiline=False,
            size_hint_y=None,
            height=50
        )

        self.class_input = TextInput(
            hint_text="Enter your class (5-10)",
            multiline=False,
            input_filter="int",
            size_hint_y=None,
            height=50
        )
        
        self.class_feedback = Label(
            text="",
            font_size=16
        )

        start = Button(
            text="Start Quiz",
            font_size=20,
            size_hint_y=None,
            height=55
        )

        back = Button(
            text="Go Back",
            font_size=18,
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.name_input)
        layout.add_widget(self.class_input)
        layout.add_widget(self.class_feedback)
        layout.add_widget(start)
        layout.add_widget(back)

        self.page_layout.add_widget(layout)

        start.bind(on_press=self.begin_quiz)
        back.bind(on_press=self.home)

    def start_timer(self):
        self.time_left = 5 * 60
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)
    
    def update_timer(self, dt):
        minutes = self.time_left // 60
        seconds = self.time_left % 60

        self.timer_label.text = f"Time Left: {minutes:02d}:{seconds:02d}"

        if self.time_left <= 0:
            self.stop_timer()
            self.show_result()
            return False

        self.time_left -= 1

    def begin_quiz(self, instance):
        self.quiz_finished = False
        self.time_left = 5 * 60
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        name = self.name_input.text.strip()
        class_text = self.class_input.text.strip()

        if not name:
            self.class_feedback.text = "Please enter your name."
            return

        if not class_text:
            self.class_feedback.text = "Please enter your class."
            return

        try:
            self.selected_class = int(class_text)
        except ValueError:
            self.class_feedback.text = "Enter a valid class number."
            return

        if self.selected_class < 5 or self.selected_class > 10:
            self.class_feedback.text = "Class must be between 5 and 10."
            return

        self.student_name = name

        self.page_layout.clear_widgets()

        self.score = 0
        self.question_number = 1

        layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=30
        )

        self.question = Label(
            text="",
            font_size=22
        )

        self.timer_label = Label(
            text=f"Time Left : {minutes} : {seconds}",
            font_size=25,
            color=(1, 0, 0, 1),
            size_hint_y=None,
            height=50
        )

        self.answer = TextInput(
            hint_text="Enter your answer",
            multiline=False,
            size_hint_y=None,
            height=50
        )

        self.answer.bind(on_text_validate=self.enter_pressed)

        self.feedback = Label(
            text="",
            font_size=18
        )

        self.submit = Button(
            text="SUBMIT",
            size_hint_y=None,
            height=50
        )
        self.submit.bind(on_press=self.check_answer)

        self.next_question = Button(
            text="NEXT QUESTION",
            disabled=True,
            size_hint_y=None,
            height=50
        )
        self.next_question.bind(
            on_press=self.next_question_pressed
        )

        layout.add_widget(
            Label(
                text=f"Student: {self.student_name} | Class: {self.selected_class}",
                font_size=18
            )
        )
        
        layout.add_widget(self.timer_label)
        layout.add_widget(self.question)
        layout.add_widget(self.answer)
        layout.add_widget(self.feedback)
        layout.add_widget(self.submit)
        layout.add_widget(self.next_question)

        self.page_layout.add_widget(layout)

        self.new_question()
        self.start_timer()
        
    def enter_pressed(self, instance):
        if self.submit.disabled:
            if not self.next_question.disabled:
                self.next_question_pressed(self.next_question)
        else:
            self.check_answer(self.submit)
        
    def stop_timer(self):
        if self.timer_event is not None:
            self.timer_event.cancel()
            self.timer_event = None
            
    def show_result(self):
        if getattr(self, "quiz_finished", False):
            return

        self.quiz_finished = True
        self.stop_timer()
        self.page_layout.clear_widgets()

        layout = BoxLayout(
            orientation="vertical",
            spacing=30,
            padding=30
        )

        score = Label(
            text=f"{self.score} / 20",
            font_size=30
        )

        if self.score >= 13:
            result = "PASS"
            self.passed_quizzes += 1
        else:
            result = "FAIL"
            self.failed_quizzes += 1

        self.save_stats()
        self.save_leaderboard()

        result_label = Label(
            text=result,
            font_size=35
        )

        back = Button(
            text="Go Back to Home",
            font_size=20,
            size_hint_y=None,
            height=60
        )

        layout.add_widget(score)
        layout.add_widget(result_label)
        layout.add_widget(back)

        self.page_layout.add_widget(layout)

        back.bind(on_press=self.home)
        
    def show_leaderboard(self, instance=None):
        self.page_layout.clear_widgets()

        page = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True
        )

        layout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            spacing=10,
            padding=20
        )

        layout.bind(
            minimum_height=layout.setter("height")
        )

        try:
            with open("leaderboard.json", "r") as file:
                leaderboard = json.load(file)

            if not isinstance(leaderboard, list):
                leaderboard = []

        except (FileNotFoundError, json.JSONDecodeError):
            leaderboard = []

        valid_students = [
            student
            for student in leaderboard
            if isinstance(student, dict)
        ]

        def get_score(student):
            try:
                return int(student.get("score", 0))
            except (TypeError, ValueError):
                return 0

        valid_students.sort(
            key=get_score,
            reverse=True
        )

        if not valid_students:
            layout.add_widget(
                Label(
                    text="No leaderboard scores yet.",
                    font_size=20,
                    size_hint_y=None,
                    height=50
                )
            )

        else:
            for rank, student in enumerate(valid_students, start=1):
                name = student.get("name", "Unknown")
                student_class = student.get("class", "N/A")
                score = get_score(student)

                layout.add_widget(
                    Label(
                        text=(
                            f"Rank {rank}: {name} | "
                            f"Class {student_class} | "
                            f"{score}/20"
                        ),
                        size_hint_y=None,
                        height=50,
                        font_size=18
                    )
                )

        scroll.add_widget(layout)

        back = Button(
            text="Go Back to Home",
            font_size=18,
            size_hint_y=None,
            height=55
        )

        back.bind(on_press=self.home)

        page.add_widget(scroll)
        page.add_widget(back)

        self.page_layout.add_widget(page)
    
MathsQuizApp().run()
