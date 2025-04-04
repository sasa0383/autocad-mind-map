import sqlite3

# Modified JSON structure where all string values have been converted to dictionaries with empty nested structure
data = {
  "Calculus": {
    "Definitions": {
      "Calculus - Mathematical study of change": {
        "Sentence 1 - Calculus includes differentiation and integration": {},
        "Sentence 2 - It extends to multivariable functions and optimization": {},
        "Sentence 3 - Core tools include limits, functions, and series expansions": {}
      },
      "Function - Relationship between variables": {
        "Sentence 1 - A function formalizes how one variable depends on another": {},
        "Sentence 2 - y = f(x) expresses y as a function of x": {},
        "Sentence 3 - x is the independent variable, y is the dependent variable": {}
      },
      "Differentiation - Rate of change of a function": {
        "Sentence 1 - It measures how a function value changes with respect to its input": {},
        "Sentence 2 - The result is the derivative of the function": {}
      },
      "Integration - Accumulation of quantities": {
        "Sentence 1 - It is the inverse operation of differentiation": {},
        "Sentence 2 - Represents area under a curve in one dimension": {},
        "Sentence 3 - Can be generalized to volume and higher-order integrals": {}
      }
    },
    "Equations": {
      "Equation 1.1 - Derivative definition": {
        "ASCII": "f'(x) = lim(h→0) [f(x+h) - f(x)] / h"
      },
      "Equation 1.2 - Integral definition": {
        "ASCII": "∫ f(x) dx = F(x) + C"
      },
      "Equation 1.3 - Fundamental Theorem of Calculus": {
        "ASCII": "d/dx ∫(a to x) f(t) dt = f(x)"
      }
    },
    "Equation Terms": {
      "f'(x) - Derivative of f with respect to x": {},
      "h - Infinitesimal increment approaching zero": {},
      "∫ f(x) dx - Indefinite integral of f(x)": {},
      "F(x) - Antiderivative of f(x)": {},
      "C - Constant of integration": {}
    },
    "Components": {
      "Independent Variable - x": {},
      "Dependent Variable - y": {},
      "Function Notation - f(x)": {},
      "Limit Operator - lim(h→0)": {}
    },
    "Worked Examples": {
      "Example 1 - Differentiate f(x) = x^2": {
        "Step 1 - Apply power rule": {},
        "Step 2 - Derivative is f'(x) = 2x": {}
      },
      "Example 2 - Integrate f(x) = 2x": {
        "Step 1 - Apply reverse power rule": {},
        "Step 2 - ∫ 2x dx = x^2 + C": {}
      }
    },
    "Metadata": {
      "ComplexityLevel": 2,
      "LearningTime": "45 mins",
      "PracticalApplication": True,
      "VisualizationAvailable": True
    },
    "CrossReference": {
      "Prerequisites": ["Functions", "Limits"],
      "RelatedTopics": ["Multivariable Calculus", "Differential Equations"],
      "ProgressionPath": ["Partial Differentiation", "Multiple Integrals"]
    },
    "Partial Differentiation": {
      "Definitions": {
        "Partial Differentiation - Derivative with respect to one variable in multivariable functions": {
          "Sentence 1 - In functions of multiple variables, partial derivatives measure change with respect to one variable at a time": {},
          "Sentence 2 - Other variables are held constant": {},
          "Sentence 3 - Notation includes ∂f/∂x and ∂f/∂y": {}
        }
      },
      "Equations": {
        "Equation 1.4 - Partial derivative with respect to x": {
          "ASCII": "∂f/∂x = lim(Δx→0) [f(x+Δx, y) - f(x, y)] / Δx"
        },
        "Equation 1.5 - Partial derivative with respect to y": {
          "ASCII": "∂f/∂y = lim(Δy→0) [f(x, y+Δy) - f(x, y)] / Δy"
        }
      },
      "Equation Terms": {
        "∂f/∂x - Partial derivative of f with respect to x": {},
        "∂f/∂y - Partial derivative of f with respect to y": {},
        "Δx, Δy - Infinitesimal changes in x and y": {}
      },
      "Worked Examples": {
        "Example - Partial derivatives of f(x, y) = x^2 + y^2": {
          "Step 1 - Compute ∂f/∂x = 2x": {},
          "Step 2 - Compute ∂f/∂y = 2y": {}
        }
      },
      "Metadata": {
        "ComplexityLevel": 3,
        "LearningTime": "30 mins",
        "PracticalApplication": True,
        "VisualizationAvailable": True
      },
      "CrossReference": {
        "Prerequisites": ["Single-variable Differentiation"],
        "RelatedTopics": ["Gradient", "Jacobian Matrix"],
        "ProgressionPath": ["Multiple Integrals", "Vector Calculus"]
      }
    },
    "Multiple Integrals": {
      "Definitions": {
        "Multiple Integrals - Extension of integration to multiple variables": {
          "Sentence 1 - Multiple integrals generalize single-variable integration": {},
          "Sentence 2 - Used to compute area, volume, and higher-dimensional quantities": {},
          "Sentence 3 - Integrals are taken with respect to one variable at a time": {}
        }
      },
      "Equations": {
        "Equation 1.6 - Double integral over region R": {
          "ASCII": "∬_R f(x, y) dx dy"
        },
        "Equation 1.7 - Triple integral for volume": {
          "ASCII": "∭_V f(x, y, z) dx dy dz"
        }
      },
      "Equation Terms": {
        "∬_R - Double integral over region R": {},
        "∭_V - Triple integral over volume V": {},
        "dx, dy, dz - Differential volume elements": {}
      },
      "Worked Examples": {
        "Example - Compute ∬_R x + y over square region [0,1] x [0,1]": {
          "Step 1 - Set up integral: ∫₀¹ ∫₀¹ (x + y) dx dy": {},
          "Step 2 - Integrate w.r.t x: ∫₀¹ [x^2/2 + xy]₀¹ dy": {},
          "Step 3 - Integrate w.r.t y: ∫₀¹ (1/2 + y) dy = 1/2 + 1/2 = 1": {}
        }
      },
      "Metadata": {
        "ComplexityLevel": 4,
        "LearningTime": "45 mins",
        "PracticalApplication": True,
        "VisualizationAvailable": True
      },
      "CrossReference": {
        "Prerequisites": ["Single-variable Integration", "Partial Differentiation"],
        "RelatedTopics": ["Vector Fields", "Divergence Theorem"],
        "ProgressionPath": ["Calculus of Variations", "Tensor Analysis"]
      }
    },
    "Calculus of Variations": {
      "Definitions": {
        "Calculus of Variations - Optimization of functionals": {
          "Sentence 1 - Concerned with finding functions that optimize a given quantity": {},
          "Sentence 2 - Functionals map functions to scalar values": {},
          "Sentence 3 - Applications include physics, engineering, and economics": {}
        },
        "Functional - A function of functions": {
          "Sentence 1 - A functional takes an entire function as input": {},
          "Sentence 2 - Returns a scalar, such as total energy or distance": {},
          "Sentence 3 - Often expressed as an integral involving the function and its derivative": {}
        }
      },
      "Equations": {
        "Equation 1.8 - Functional definition": {
          "ASCII": "J[y] = ∫(a to b) F(x, y(x), y'(x)) dx"
        },
        "Equation 1.9 - Euler-Lagrange equation": {
          "ASCII": "∂F/∂y - d/dx (∂F/∂y') = 0"
        }
      },
      "Equation Terms": {
        "J[y] - Functional acting on function y": {},
        "F - Function of x, y, and y'": {},
        "∂F/∂y - Partial derivative of F with respect to y": {},
        "∂F/∂y' - Partial derivative of F with respect to y'": {},
        "d/dx - Total derivative with respect to x": {}
      },
      "Worked Examples": {
        "Example - Shortest path between two points (straight line)": {
          "Step 1 - Define functional for arc length: J[y] = ∫ sqrt(1 + (y')^2) dx": {},
          "Step 2 - Apply Euler-Lagrange equation": {},
          "Step 3 - Resulting differential equation yields a linear solution y = mx + c": {}
        }
      },
      "Metadata": {
        "ComplexityLevel": 5,
        "LearningTime": "60 mins",
        "PracticalApplication": True,
        "VisualizationAvailable": True
      },
      "CrossReference": {
        "Prerequisites": ["Differentiation", "Integration"],
        "RelatedTopics": ["Optimization", "Lagrangian Mechanics"],
        "ProgressionPath": ["Functional Analysis", "Differential Equations"]
      }
    }
  }
}





# Your existing database functions can remain unchanged
def create_database(db_path):
    """
    Create the database schema.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Drop existing tables
        cursor.execute("DROP TABLE IF EXISTS topics")
        cursor.execute("DROP TABLE IF EXISTS relationships")

        # Create tables
        cursor.execute("""
        CREATE TABLE topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            level INTEGER NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE relationships (
            parent_id INTEGER NOT NULL,
            child_id INTEGER NOT NULL,
            FOREIGN KEY (parent_id) REFERENCES topics(id),
            FOREIGN KEY (child_id) REFERENCES topics(id)
        )
        """)

def populate_database(data, db_path):
    """
    Populate the database with hierarchical data.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        def add_node(name, level, parent_id=None):
            cursor.execute("INSERT INTO topics (name, level) VALUES (?, ?)", (name, level))
            node_id = cursor.lastrowid
            if parent_id:
                cursor.execute("INSERT INTO relationships (parent_id, child_id) VALUES (?, ?)", (parent_id, node_id))
            return node_id

        def traverse_tree(tree, level=0, parent_id=None):
            x_offset = 0  # Start x-offset for sibling spacing
            spacing = 1   # Adjustable spacing between siblings

            for name, children in tree.items():
                node_id = add_node(name, level, parent_id)

                if isinstance(children, dict):
                    # Recursive traversal for nested dictionaries
                    traverse_tree(children, level + 1, node_id)
                elif isinstance(children, list):
                    for child in children:
                        add_node(child, level + 1, node_id)

                x_offset += spacing

        traverse_tree(data)

if __name__ == "__main__":
    db_path = "tree_structure.db"
    create_database(db_path)
    populate_database(data, db_path)
    print("Database created and populated successfully.")