import sublime
import sublime_plugin

class InsertAsTagCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      word_reg = self.view.word(region)
      word = self.view.substr(word_reg)
      if not word:
        word = "p"
      s = "<%s></%s>" % (word, word)
      self.view.replace(edit, word_reg, s)
