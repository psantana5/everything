#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <curl/curl.h>

// Function to execute a shell command and get the output
std::string executeCommand(const std::string &command)
{
    char buffer[128];
    std::string result = "";
    FILE *pipe = _popen(command.c_str(), "r");
    if (!pipe)
        return "ERROR";
    while (fgets(buffer, sizeof(buffer), pipe) != NULL)
    {
        result += buffer;
    }
    _pclose(pipe);
    return result;
}

// Function to download the audio from a YouTube URL
bool downloadAudio(const std::string &url)
{
    std::string command = "youtube-dl --extract-audio --audio-format mp3 -o \"audio.mp3\" " + url;
    std::string output = executeCommand(command);
    return (output.find("ERROR") == std::string::npos);
}

// Function to download the video from a YouTube URL
bool downloadVideo(const std::string &url)
{
    std::string command = "youtube-dl -f \"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best\" -o \"video.mp4\" " + url;
    std::string output = executeCommand(command);
    return (output.find("ERROR") == std::string::npos);
}

int main()
{
    std::string url;
    std::cout << "Enter the YouTube video URL: ";
    std::getline(std::cin, url);

    // Download audio and video
    bool audioDownloaded = downloadAudio(url);
    bool videoDownloaded = downloadVideo(url);

    if (audioDownloaded && videoDownloaded)
    {
        std::cout << "Download completed.\n";
    }
    else
    {
        std::cout << "Failed to download audio or video.\n";
    }

    return 0;
}
