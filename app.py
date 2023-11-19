import gradio as gr

def greet(name: str) -> str:
    """ Function that takes a name and returns a greeting """
    return f"Hello {name}!"

# Create the Gradio interface
interface = gr.Interface(fn=greet, 
                         inputs=gr.inputs.Textbox(lines=2, placeholder="Type your name..."), 
                         outputs="text")

# Launch the app
interface.launch()

