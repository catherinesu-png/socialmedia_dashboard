from matplotlib import pyplot as plt 
from matplotlib import dates as mpdates

metrics = ["New Followers", "Accounts Engaged","Content Engagement" , "Impressions/views", "Profile Visits", "Reach" ]

def plot_new_followers(df):
    engagement_metric = "New Followers"
    make_plot(df, engagement_metric)
    
def plot_reach(df):
    engagement_metric = "Reach"
    make_plot(df, engagement_metric)

def plot_impressions(df):
    engagement_metric = "Impressions/views"
    make_plot(df, engagement_metric)
    
def plot_prof_visits(df):
    engagement_metric = "Profile Visits"
    make_plot(df, engagement_metric)
    
def plot_accounts_engaged(df):
    engagement_metric = "Accounts Engaged"
    make_plot(df, engagement_metric)
    
def plot_content_engagement(df):
    engagement_metric = "Content Engagement"
    make_plot(df, engagement_metric)
    
def plot_one_metric(df, engagement_metric): 
    fig, ax = plt.subplots(figsize=(14,6))
    make_plot(ax, df, engagement_metric)
    plt.tight_layout()
    plt.show()
    
def plot_all_metrics(df): 
    fig, axs = plt.subplots(2,3, figsize=(18,10), sharex = False)
    axs= axs.flatten()
    
    for i, metric in enumerate(metrics):
        ax = axs[i]
        make_plot(ax, df, metric)
        #TODO add error checking? 
    fig.suptitle("Instagram Engagement Metrics over Time", fontsize = 20)
    plt.tight_layout()
    plt.show()
    
def make_plot(ax, df, engagement_metric): 
    """
    Plot the given engagement metric on the given Axes object 
    """

    ax.plot(df["Week"], df[engagement_metric], marker = "o", label = engagement_metric)
    ax.set_title(engagement_metric + " Over Time")
    ax.set_xlabel("Week")
    ax.set_ylabel(engagement_metric)
    
    ax.xaxis.set_major_locator(mpdates.MonthLocator(bymonthday = 1 )) #interval = 2 let's see how it looks first
    ax.xaxis.set_major_formatter(mpdates.DateFormatter("%b %Y"))
    ax.tick_params(axis = "x", rotation = 45)
    
    ax.grid(True)
    
    
