import time, sys

time_start_progress_bar = 0

def ShowProgressBar(entry, MaxEntry, PercentagePrecision = 5):
    NStep = int(100/PercentagePrecision)
    StepSize = int(MaxEntry/NStep)

    if entry%StepSize==0:
        if entry>0:
            sys.stdout.write('\r')
        else:
            global time_start_progress_bar
            time_start_progress_bar = time.time()

        Progress = float(entry)/MaxEntry
        #print Progress
        NStepDone = int(Progress*NStep)

        OutLine = '['+'#'*NStepDone + '-'*(NStep-NStepDone) +']'+'  {0}%'.format(int(100*Progress))
        sys.stdout.write(OutLine)
        sys.stdout.flush()

        if entry>0:
            timeleft = (MaxEntry - float(entry))*(time.time() - time_start_progress_bar)/float(entry)
            if timeleft<181:
                sys.stdout.write(" - remaning:{:5.0f} s   ".format(timeleft))
            elif timeleft<10801:
                timeleft/=60
                sys.stdout.write(" - remaning:{:5.1f} min ".format(timeleft))
            else:
                timeleft/=3600
                sys.stdout.write(" - remaning:{:5.1f} h   ".format(timeleft))

            sys.stdout.flush()

    if entry==MaxEntry-1:
        OutLine = '\r['+ '#'*NStep +']  100%'+20*' '+'\n'
        sys.stdout.write(OutLine)
        print "Elapsed time {:.1f} sec (wall time)".format(time.time() - time_start_progress_bar)
