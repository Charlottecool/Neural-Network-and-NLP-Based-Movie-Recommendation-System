import gradio as gr

def combined_user_and_movie_recommendation(user_input):
    """
    Combines recommendations based on user ID and movie title.
    If user input is an ID, it returns user-based recommendations.
    If user input is a movie title, it returns content-based recommendations.
    
    Parameters:
    user_input (str): User input, either a user ID or a movie title.
    
    Returns:
    A string with recommended movie titles or an error message if movie title not found.
    """
    try:
        # Try to parse the input as a user ID (integer)
        user_id = int(user_input)
        # Use SVD-based recommendation for user ID
        user_recommendations = get_user_based_recommendations(user_id, final_merged_data, best_svd, n_recommendations=5)
        return "\n".join(user_recommendations)
    
    except ValueError:
        # If the input is not a number, treat it as a movie title
        try:
            # Directly call combined_recommendation_v2 without converting or checking manually
            movie_recommendations = combined_recommendation_v2(user_input, merged_data_copy, movie_embeddings, n_recommendations=5)
            return "\n".join(movie_recommendations)
        except ValueError:
            # If combined_recommendation_v2 raises a ValueError, return "Oops"
            return "Oops, no movie found with a title similar to '{}'.".format(user_input)


# Create Gradio interface with a single input for user ID or movie title
interface = gr.Interface(
    fn=combined_user_and_movie_recommendation,
    inputs=gr.Textbox(label="Enter User ID or Movie Title"),
    outputs=gr.Textbox(label="Recommended Movies"),
    title="Charlotte's Movie Recommendation System 2.0",
    description="Enter a user ID for personalized recommendations, or a movie title for content-based recommendations."
)

# Launch the Gradio interface
interface.launch()