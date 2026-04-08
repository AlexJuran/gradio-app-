import gradio as gr

def greet(name):
    return "Labdien, jūs esat reģistrēts kā lietotājs: " + name

demo = gr.Interface(
    fn=greet,
    inputs="textbox",
    outputs="textbox"
)

if __name__ == "__main__":
    demo.launch()
