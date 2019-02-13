import time, sys

class ProgressBar(object):
    self.time_start_progress_bar = 0
    self.last_displyed_time = 0
    self.PercentagePrecision = 5
    self.MaxEntry = 0

    def __init__(self, max_entries, perc_precision = 5):
        self.time_start_progress_bar = 0
        self.last_displyed_time = 0
        self.PercentagePrecision = perc_precision
        self.MaxEntry = max_entries


    def PrintUpdate(self,entry, self.MaxEntry):
        NStep = int(100/PercentagePrecision)
        StepSize = int(self.MaxEntry/NStep)

        timeleft = (self.MaxEntry - float(entry))*(time.time() - self.time_start_progress_bar)/float(entry)
        rel_time_change = (self.last_displyed_time - timeleft)/self.last_displyed_time
        if entry%StepSize==0 or rel_time_change>0.05:
            if entry>0:
                sys.stdout.write('\r')
            else:
                self.time_start_progress_bar = time.time()

            Progress = float(entry)/self.MaxEntry
            #print Progress
            NStepDone = int(Progress*NStep)

            OutLine = '['+'#'*NStepDone + '-'*(NStep-NStepDone) +']'+'  {0}%'.format(int(100*Progress))
            sys.stdout.write(OutLine)
            sys.stdout.flush()

            if entry>0:
                self.last_displyed_time = timeleft
                if timeleft<181:
                    sys.stdout.write(" - remaning:{:5.0f} s   ".format(timeleft))
                elif timeleft<10801:
                    timeleft/=60
                    sys.stdout.write(" - remaning:{:5.1f} min ".format(timeleft))
                else:
                    timeleft/=3600
                    sys.stdout.write(" - remaning:{:5.1f} h   ".format(timeleft))

                sys.stdout.flush()

        if entry==self.MaxEntry-1:
            OutLine = '\r['+ '#'*NStep +']  100%'+20*' '+'\n'
            sys.stdout.write(OutLine)
            print "Elapsed time {:.1f} sec (wall time)".format(time.time() - self.time_start_progress_bar)
