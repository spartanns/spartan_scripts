import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy import VideoFileClip


class VideoEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Video Editor")

        self.video_path = None
        self.clip = None

        # UI Components
        self.label = tk.Label(root, text="Select a video to get started")
        self.label.pack(pady=10)

        self.select_button = tk.Button(
            root, text="Select Video", command=self.select_video
        )
        self.select_button.pack(pady=5)

        self.start_label = tk.Label(root, text="Start Time (in seconds):")
        self.start_label.pack(pady=5)
        self.start_entry = tk.Entry(root)
        self.start_entry.pack(pady=5)

        self.end_label = tk.Label(root, text="End Time (in seconds):")
        self.end_label.pack(pady=5)
        self.end_entry = tk.Entry(root)
        self.end_entry.pack(pady=5)

        self.trim_button = tk.Button(
            root, text="Trim Video", command=self.trim_video, state=tk.DISABLED
        )
        self.trim_button.pack(pady=10)

        self.export_button = tk.Button(
            root, text="Export Video", command=self.export_video, state=tk.DISABLED
        )
        self.export_button.pack(pady=5)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv")]
        )
        if self.video_path:
            self.clip = VideoFileClip(self.video_path)
            self.label.config(text=f"Selected Video: {self.video_path.split('/')[-1]}")
            self.trim_button.config(state=tk.NORMAL)

    def trim_video(self):
        try:
            start_time = float(self.start_entry.get())
            end_time = float(self.end_entry.get())
            if (
                start_time < 0
                or end_time > self.clip.duration
                or start_time >= end_time
            ):
                raise ValueError("Invalid start or end time.")
            self.trimmed_clip = self.clip.subclipped(start_time, end_time)
            messagebox.showinfo(
                "Success", "Video trimmed successfully! Ready to export."
            )
            self.export_button.config(state=tk.NORMAL)
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def export_video(self):
        output_path = filedialog.asksaveasfilename(
            defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")]
        )
        if output_path:
            self.trimmed_clip.write_videofile(output_path)
            messagebox.showinfo("Success", "Video exported successfully!")


# Create the Tkinter app
root = tk.Tk()
app = VideoEditor(root)
root.mainloop()
