//C++ INCLUDES
//ROOT INCLUDES
//LOCAL INCLUDES
#include "CommandLineInput.hh"

std::string ParseCommandLine( int argc, char* argv[], std::string opt )
{
  for (int i = 1; i < argc; i++ )
    {
      std::string tmp( argv[i] );
      if ( tmp.find( opt ) != std::string::npos )
        {
          return tmp.substr( tmp.find_last_of("=") + 1 );
        }
    }

  return "";
};
