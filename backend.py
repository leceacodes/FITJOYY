from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import json

class FitJoyHandler(SimpleHTTPRequestHandler):
    # For simplicity, using a dictionary to store user data.
    users = {}

    def do_GET(self):
        # Respond to a GET request with fitness-related features.
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Define fitness-related features
        features = {
            "fitness_goals": "Set and track personalized fitness goals.",
            "workout_routines": "Access diverse workout routines for all fitness levels.",
            "nutrition_recommendations": "Receive tailored nutrition recommendations.",
            "social_elements": "Connect with friends, share achievements, and join fitness challenges.",
            "positive_mindset": "Promote a positive mindset by celebrating progress and fostering a supportive community.",
            "user_authentication": "Register and log in to save and track your fitness journey.",
            "personalized_workouts": "Get personalized workout recommendations based on your fitness level and preferences.",
            "progress_tracking": "Track your fitness progress over time.",
        }

        response_data = {"features": features}
        self.wfile.write(json.dumps(response_data).encode())

    def do_POST(self):
        # Handle user registration data sent via POST request.
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        user_data = json.loads(post_data.decode())

        # For simplicity, storing user data in memory. In a real app, use a database.
        user_id = user_data.get("user_id")
        if user_id:
            self.users[user_id] = user_data

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {"message": "Data received successfully."}
        self.wfile.write(json.dumps(response_data).encode())

if __name__ == "__main__":
    # Run the server on port 8000
    with TCPServer(("", 8000), FitJoyHandler) as httpd:
        print("Server started on port 8000.")
        httpd.serve_forever()
