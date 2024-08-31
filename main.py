import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyAisUoMJ1iJEZEd0mpr8AwLIz9H_o0Cvdw')
# Upload the file and print a confirmation.
sample_file = genai.upload_file(path="au-t-1634079864-australian-editable-sample-timetable_ver_1.jpg",
                            display_name="Time Table")

print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Prompt the model with text and the previously uploaded image.
prompt = """        Parse this class schedule image and return the information in a structured format.
        For each class entry, provide the following details:
        - Day of the week
        - Start time
        - End time
        - Class name
        - Location (if available)

        Format the output as follows:
        Day: [Day of the week]
        Start Time: [Start time]
        End Time: [End time]
        Class: [Class name]
        Location: [Location or "N/A" if not provided]

        Repeat this structure for each class entry in the schedule.
        If any information is unclear or not provided in the image, mark it as "Unknown"."""
response = model.generate_content([sample_file, prompt])

print(">" + response.text)