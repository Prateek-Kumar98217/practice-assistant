from subgraphs.main_sg import MainSubgraphBuilder
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from tools.calculator import run_tool as calculator_tool
from tools.weather import run_tool as weather_tool

load_dotenv()

tools=[calculator_tool, weather_tool]

# Initialize LLMs
planner_llm = init_chat_model("google_genai:gemini-2.5-flash").bind(tools=tools)
memory_llm = init_chat_model("google_genai:gemini-2.5-flash")
synth_llm = init_chat_model("google_genai:gemini-2.5-flash", temperature=0.6)

# Build the full graph
main_graph = MainSubgraphBuilder(planner_llm, synth_llm, memory_llm).build()

# Chat loop state
messages = []
memories = ""

print("🤖 Dev-sama is ready. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Dev-sama: Goodbye!")
        break

    messages.append(user_input)
    state_input = {
        "messages": messages,
        "memories": memories,
    }

    try:
        final_state = main_graph.invoke(state_input)
        output = final_state.get("final_output", "⚠️ No response generated.")
        print(f"Dev-sama: {output}")

        # update state
        messages = final_state.get("messages", messages)
        memories = final_state.get("memories", memories)

    except Exception as e:
        print("❌ Error during execution:", e)
