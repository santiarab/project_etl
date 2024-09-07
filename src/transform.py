import pandas as pd

def best_goal_diff(df: pd.DataFrame, top=5) -> pd.DataFrame:
    df["HomeGoals"] = df["HomeGoals"].astype(int)
    df["AwayGoals"] = df["AwayGoals"].astype(int)
    df['GoalDifference'] = abs(df['HomeGoals'] - df['AwayGoals'])
    best_df = df.sort_values(by='GoalDifference', ascending=False).reset_index()
    best_df_part = best_df[['Year', 'Round', 'Country', 'HomeTeam', 'HomeGoals', 'AwayGoals', 'AwayTeam']]
    print(best_df_part.head(top))
    return best_df_part

